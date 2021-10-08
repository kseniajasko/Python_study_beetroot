# Extend the echo server, which returns to client the data, encrypted using
# the Caesar cipher algorithm by a specific key obtained from the client.

import socket
import json

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 6789        # Port to listen on (non-privileged ports are > 1023)
addr = (HOST,PORT)

# we will be listening for UDP messages
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

def encypt_func(txt, s):
    result = ""
    # transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        # encypt_func uppercase characters in plain txt
        if (char.isupper()):
            result += chr((ord(char) + s - 64) % 26 + 65)
            # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) + s - 96) % 26 + 97)
    return result

while True:

    data, addr = sock.recvfrom(1024)
    print('client addr: ', addr)
    data = bytes.decode(data)
    data = json.loads(data)
    text = data[0]
    key = data[1]
    text = str.encode(encypt_func(text, key))
    print(text)
    sock.sendto(text, addr)

