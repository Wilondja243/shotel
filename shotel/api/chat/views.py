from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from shotel.app.chat.models import Message, Conversation
from shotel.api.chat.serializers import (
    MessageSerializer,
    ConversationSerializer
)


class ConversationListView(ListAPIView):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return self.request.user.conversations.all() \
                .prefetch_related('participants')
    
