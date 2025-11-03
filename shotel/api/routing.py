from django.urls import path

from shotel.app.consummers import Consommer


websocket_urlpatterns = [
    path('ws/entry/', Consommer.as_asgi()),
]