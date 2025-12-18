from django.urls import path, re_path

from shotel.api.chat.consummers import ChatConsumer


websocket_urlpatterns = [
    path('ws/chat/<uuid:user_id>/', ChatConsumer.as_asgi()),
]