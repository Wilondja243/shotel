import json
from channels.generic.websocket import AsyncWebsocketConsumer


class Consommer(AsyncWebsocketConsumer):
    async def connect(self):
        pass

    async def disconnect(self, code):
        pass

    async def receive(self, text_data):
        pass
