from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from shotel.api.chat.serializers import ChatSerializer
from shotel.app.chat.models import Message
from shotel.app.chat.conversation import get_or_create_conversation


class ChatAPIView(APIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated,]


class SendMessageAPIView(APIView):
    def post(self, request):
        text = request.data.get('text')
        target_user_id = request.data.get('receiver_id')

        other_user = get_object_or_404(settings.AUTH_USER_MODEL, id=target_user_id)

        conversation = get_or_create_conversation(request.user, other_user)

        Message.objects.create(
            conversation=conversation,
            sender=request.user,
            text=text
        )

        return Response(
            {
                'message': "Publication aimée avec success",
                'conv_id': conversation.id
            },
            status=status.HTTP_201_CREATED
        )
