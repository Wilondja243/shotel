from shotel.app.chat.models import Chat
from rest_framework import serializers
from shotel.api.serializers import UserMiniSerializer


class ChatSerializer(serializers.ModelSerializer):
    sender = UserMiniSerializer(read_only=True)
    receiver = UserMiniSerializer(ready_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'message']