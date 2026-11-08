
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse

from .tasks import test_background_task
from celery.result import AsyncResult


def test(request):

    # Submit task to Celery worker
    test_background_task.delay("Matinabbasso@gmail.com")
    
    return HttpResponse(
        f"""
        <html>
            <head>
                <title>Nexora Celery Test</title>
            </head>

            <body>
                <h1>Nexora Background Task</h1>

                <p>Task submitted successfully!</p>

               
                </p>
            </body>
        </html>
        """
    )



urlpatterns = [
    path("admin/", admin.site.urls),

    path("", test, name="test"),

   
]
