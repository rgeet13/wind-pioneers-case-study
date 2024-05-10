from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Process the message and prepare a response
        response_message = f"Server received: {message}"
        print(response_message)

        # Send the response back to the client
        await self.send(text_data=json.dumps({
            'message': response_message
        }))
