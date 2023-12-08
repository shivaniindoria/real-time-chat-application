import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f'room_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        data = { 'type':'connected'}
        self.send(text_data=json.dumps({'payload':'connected'}))

    def receive(self, text_data):
        pass
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # sender = text_data_json['sender']

        # self.send(text_data=json.dumps({
        #     'message': message,
        #     'sender': sender
        # }))

    def disconnect(self, close_code):
        pass
