import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .services import broadcast_test_event


@login_required
@ensure_csrf_cookie
def websocket_test_page(request):

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nexora WebSocket Test</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
            }

            #events {
                margin-top: 20px;
                padding: 15px;
                border: 1px solid #ccc;
                min-height: 150px;
            }

            input {
                padding: 10px;
                width: 250px;
            }

            button {
                padding: 10px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>

        <h2>Nexora WebSocket Test</h2>

        <p>Status: <strong id="status">Connecting...</strong></p>

        <input
            type="text"
            id="message"
            placeholder="Enter your message"
        >

        <button onclick="sendMessage()">
            Send Broadcast
        </button>

        <h3>Received Events</h3>

        <div id="events"></div>

        <script>

            const statusElement = document.getElementById("status");
            const eventsElement = document.getElementById("events");

            function addEvent(data) {
                const item = document.createElement("p");
                item.textContent = JSON.stringify(data);
                eventsElement.appendChild(item);
            }

            const protocol =
                window.location.protocol === "https:" ? "wss:" : "ws:";

            const socket = new WebSocket(
                protocol + "//" + window.location.host + "/ws/"
            );

            socket.onopen = function() {
                statusElement.textContent = "Connected";
            };

            socket.onmessage = function(event) {
                const data = JSON.parse(event.data);
                addEvent(data);
            };

            socket.onerror = function(error) {
                statusElement.textContent = "WebSocket error";
                console.error(error);
            };

            socket.onclose = function(event) {
                statusElement.textContent =
                    "Disconnected (code " + event.code + ")";
            };

            function getCookie(name) {
                let cookieValue = null;

                if (document.cookie) {
                    const cookies = document.cookie.split(";");

                    for (let cookie of cookies) {
                        cookie = cookie.trim();

                        if (cookie.startsWith(name + "=")) {
                            cookieValue = decodeURIComponent(
                                cookie.substring(name.length + 1)
                            );
                            break;
                        }
                    }
                }

                return cookieValue;
            }

            async function sendMessage() {

                const message =
                    document.getElementById("message").value.trim();

                if (!message) {
                    alert("Enter a message first.");
                    return;
                }

                try {

                    const response = await fetch("/websocket-test/", {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": getCookie("csrftoken")
                        },

                        credentials: "same-origin",

                        body: JSON.stringify({
                            message: message
                        })
                    });

                    const result = await response.json();

                    if (!response.ok) {
                        throw new Error(
                            result.message || "Broadcast request failed"
                        );
                    }

                    console.log("Broadcast:", result);

                    document.getElementById("message").value = "";

                } catch (error) {
                    console.error(error);
                    alert(error.message);
                }
            }

        </script>

    </body>
    </html>
    """

    return HttpResponse(html)


@login_required
@require_POST
@csrf_protect
def websocket_test(request):

    try:
        data = json.loads(request.body)

        message = data.get("message", "")

        if not isinstance(message, str) or not message.strip():
            return JsonResponse({
                "status": "error",
                "message": "Message is required."
            }, status=400)

        broadcast_test_event(message.strip())

        return JsonResponse({
            "status": "success",
            "message": "Broadcast sent.",
            "data": message.strip()
        })

    except json.JSONDecodeError:

        return JsonResponse({
            "status": "error",
            "message": "Invalid JSON."
        }, status=400)