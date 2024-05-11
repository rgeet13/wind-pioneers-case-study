from channels.generic.websocket import AsyncWebsocketConsumer
import json, os
from django.conf import settings
from .drive_utils import get_all_files_from_folder, create_service, download_file
from .gpt_utils import upload_file, create_assistant, create_vector_store_and_upload_files, update_assistant, create_thread, get_response

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        query_params = self.scope['query_string'].decode()
        file_name = None
        if query_params:
            params = dict(q.split('=') for q in query_params.split('&'))
            file_name = params.get('file_name')
        file_path = os.path.join(settings.BASE_DIR, file_name)
        vector_store_id = create_vector_store_and_upload_files(file_path)
        assistant = create_assistant()
        print('Assistant created:', assistant)
        updated_assistant = update_assistant(assistant.id, vector_store_id)
        print('Assistant updated:', updated_assistant)
        # thread = create_thread(file_path, "What is the document about ?")
        # print('Thread created:', thread)
        # response = get_response(updated_assistant.id, thread.id)
        # print('Response:', response)
        self.updated_assistant_id = updated_assistant.id
        self.file_path = file_path

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'message' in text_data_json:
            message = text_data_json['message']
            thread = create_thread(self.file_path, message)
            response_message = f"Server Sent: {get_response(self.updated_assistant_id, thread.id)}"
            # test = get_all_files_from_folder('13KSB55spACO_PyBswteQgiIZGm2ZRq2Q')
            # test = download_file("1gSaujCfMHwaMlbiTvyId7ST25ltBf0jj", "Marksheet.pdf")
            # print(type(test))
            await self.send(text_data=json.dumps({
                'message': response_message
            }))
