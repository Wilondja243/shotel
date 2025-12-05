import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

# from shotel.app.chat.models import Chat


class Consommer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connexion établie!"}))

    async def disconnect(self, code):
        print("websocket closed")
        await self.send(text_data=json.dumps({"message": "Socket disconnect succefuly"}))

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        # users = self.get_users()

        await self.send(text_data=json.dumps({"message": message}))

    # @database_sync_to_async
    # def get_users(self):
    #     return Chat.objects.all()