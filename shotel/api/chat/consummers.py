import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']

        if self.user.is_anonymous:
            self.close()
            return
        
        self.other_user_id = self.scope['url_route']["kwargs"]['user_id']

        ids = sorted([str(self.user.id), str(self.other_user_id)])
        self.room_name = f"chat_{ids[0]}_{ids[1]}"
        self.room_group_name = f"group_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connexion établie!"}))

    async def disconnect(self, code):
        if hasattr(self, 'room_group_name'):
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
                "sender_id": str(self.user.id)
            }
        )
    
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender_id": event["sender_id"]
        }))

    @database_sync_to_async
    def save_message(self, message):
        from django.contrib.auth import get_user_model
        from shotel.app.chat.models import Message

        User = get_user_model

        try:
            other_user = User.objects.get(id=self.other_user_id)

            from shotel.app.chat.conversation import get_or_create_conversation
            conversation = get_or_create_conversation(self.user, other_user)

            Message.objects.create(
                conversation=conversation,
                sender = self.user,
                message = message
            )
        except Exception as e:
            print(f"Error to save message: {e}")