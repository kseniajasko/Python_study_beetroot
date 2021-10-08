import socket
import sys

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 6789        # Port to listen on (non-privileged ports are > 1023)
addr = (HOST,PORT)

# we will be listening for UDP messages
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)


while True:

    data, addr = sock.recvfrom(1024)
    print('client addr: ', addr)
    print(data)
    sock.sendto(data.upper(), addr)





