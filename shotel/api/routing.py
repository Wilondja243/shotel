from django.urls import path, re_path

from shotel.api.chat.consummers import ChatConsummer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_id>[0-9a-f-]+)/$', ChatConsummer.as_asgi()),
]