# import socket
# from multiprocessing import Process
#
#
# def communicate(sock):
#     while True:
#         data = sock.recv(1024)
#         print(data.decode('utf8'))
#         sock.send(data.upper())
#
#
# if __name__ == '__main__':
#     server = socket.socket()
#     server.bind(('127.0.0.1', 8080))
#     server.listen(5)
#     while True:
#         sock, addr = server.accept()
#         p = Process(target=communicate, args=(sock,))
#         p.start()


import socket
from multiprocessing import Process
from threading import Thread

server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)

def communicate(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        sock.send(data.upper())

while True:
    sock, addr = server.accept()
    p = Thread(target=communicate, args=(sock,))
    p.start()