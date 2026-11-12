from channels.generic.websocket import AsyncJsonWebsocketConsumer


class GlobalConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope["user"]

        # Require a logged-in user
        if not user.is_authenticated:
            await self.close(code=4001)
            return

        self.user_group = f"user_{user.pk}"
        self.test_group = "test_room"

        # Join the groups
        await self.channel_layer.group_add(
            self.user_group,
            self.channel_name
        )

        await self.channel_layer.group_add(
            self.test_group,
            self.channel_name
        )

        await self.accept()

        await self.send_json({
            "type": "connection.established",
            "message": "Connected successfully"
        })

        print(f"WebSocket connected: user {user.pk}")

    async def disconnect(self, close_code):

        if hasattr(self, "user_group"):
            await self.channel_layer.group_discard(
                self.user_group,
                self.channel_name
            )

        if hasattr(self, "test_group"):
            await self.channel_layer.group_discard(
                self.test_group,
                self.channel_name
            )

        print("WebSocket disconnected:", close_code)

    async def receive_json(self, content, **kwargs):

        await self.send_json({
            "type": "request.received",
            "data": content
        })

    async def realtime_event(self, event):

        await self.send_json({
            "type": event["event"],
            "data": event["data"]
        })