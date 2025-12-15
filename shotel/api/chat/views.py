from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shotel.api.chat.serializers import ChatSerializer


class ChatAPIView(APIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated,]

    