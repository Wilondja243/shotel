import json
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.other_user_id = self.scope['url_route']["kwargs"]['user_id']

        self.room_name = f"chat_{min(self.user.id, self.other_user_id)}_{max(self.user.id, self.other_user_id)}"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connexion établie!"}))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")

        await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender_id": self.user.id
            }
        )

    @database_sync_to_async
    def save_message(self, message):
        from shotel.app.user.models import User
        from shotel.app.chat.models import Message
        from shotel.app.chat.conversation import get_or_create_conversation
        
        other_user = get_object_or_404(User, id=self.other_user_id)
        conversation = get_or_create_conversation(self.user, other_user)

        Message.objects.create(
            conversation=conversation,
            sender = self.user,
            message = message
        )