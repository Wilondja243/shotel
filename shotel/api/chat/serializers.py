from shotel.app.chat.models import Message
from rest_framework import serializers
from shotel.api.serializers import UserMiniSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserMiniSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message', 'is_ready']