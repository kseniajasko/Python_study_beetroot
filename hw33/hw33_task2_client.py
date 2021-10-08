import socket
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6789        # The port used by the server
addr = (HOST, PORT)
message = "Hello world"
key = 5
data = [message, key]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = json.dumps(data)
data = str.encode(data)
s.sendto(data, addr)
data = bytes.decode(data)
data, addr = s.recvfrom(1024)
data = bytes.decode(data)
print(data)




