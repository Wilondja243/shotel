from django.urls import path

from shotel.app.consummers import Consommer


websocket_urlpatterns = [
    path('ws/api/test/', Consommer.as_asgi()),
]