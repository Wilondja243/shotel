from django.urls import path, re_path

from shotel.api.chat.consummers import ChatConsumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_id>[0-9a-f-]+)/$', ChatConsumer.as_asgi()),
]