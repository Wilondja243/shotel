from rest_framework import serializers
from shotel.app.user.models import User
from shotel.api.serializers import UserMiniSerializer
from shotel.app.chat.models import (
    Message,
    Conversation
)


class MessageSerializer(serializers.ModelSerializer):
    sender = UserMiniSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message', 'is_ready']


class ConversationSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField(read_only=True)
    other_user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'other_user', 'last_message']

    def get_other_user(self, obj):
        request_user = self.context['request'].user
        other_user = obj.participants.exlude(id=request_user.id).first()

        if other_user:
            return {
                "id": other_user.id,
                "username": other_user.username,
                "avatar": other_user.profile.avatar.url if hasattr(other_user, 'profile') else None
            }
        return None

    def get_last_message(self, obj):
        last_msg = obj.messages.last()
        if last_msg:
            return {
                "message": last_msg.message,
                "sender_id": last_msg.sender.id,
                "created_at": last_msg.created_at,
            }
        return None
