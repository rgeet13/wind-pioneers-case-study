from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.conf import settings
from .drive_utils import get_all_files_from_folder, create_service, download_file

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response_message = f"Server Sent: {message}"
        # test = get_all_files_from_folder('13KSB55spACO_PyBswteQgiIZGm2ZRq2Q')
        # test = download_file("1gSaujCfMHwaMlbiTvyId7ST25ltBf0jj", "Marksheet.pdf")
        # print(type(test))
        await self.send(text_data=json.dumps({
            'message': 'test'
        }))
