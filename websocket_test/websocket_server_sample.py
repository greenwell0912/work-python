#!/usr/bin/env python
import msgpack
import base64
from websocket_server import WebsocketServer

def new_client(client, server):
    #server.send_message_to_all("Hey all, a new client has joined us")
    pass

def send_msg_allclient(client, server,message):
    #server.send_message_to_all("Hey all:"+message)
 
    data = msgpack.packb([1,2,3], use_bin_type=True)
    print(data)
    a = base64.b64encode(data)
    server.send_message_to_all(a)

server = WebsocketServer(12345, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_message_received(send_msg_allclient)
server.run_forever()
