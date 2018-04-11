import time
import msgpack
import base64
from websocket import create_connection

ws = create_connection("ws://127.0.0.1:12345/")

while True:
    ws.send("Hello, World")
    time.sleep(1)
    result =  ws.recv()
    result_bytes = result.encode('utf-8')
    msgpackdata = base64.b64decode(result)
    data = msgpack.unpackb(msgpackdata, use_list=False, raw=False)
    print("Received '%s'" % str(data)) 
    time.sleep(1)

ws.close()
