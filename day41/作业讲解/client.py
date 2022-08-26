# import socket
#
# client = socket.socket()
# client.connect(())
#
# while True:
#     client.send('hello'.encode('utf8'))
#     print(client.recv(1024).decode('utf8'))

import socket

client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:
    client.send(b'hello')
    print(client.recv(1024).decode('utf8'))

