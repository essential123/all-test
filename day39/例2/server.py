# import socket
# server = socket.socket(type=socket.SOCK_DGRAM)
# server.bind(('127.0.0.1', 8080))
# while True:
#     msg, addr = server.recvfrom(1024)
#     print('msg>>:', msg.decode('utf8'))
#     print('addr>>:', addr)
#     back_data = input(f'请回复{addr}客户端的消息>>:').strip()
#     server.sendto(back_data.encode('utf8'), addr)


import socket
server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))
msg, addr = server.recvfrom(1024)
print(msg.decode('utf8'), addr)
msg, addr = server.recvfrom(1024)
print(msg.decode('utf8'), addr)
msg, addr = server.recvfrom(1024)
print(msg.decode('utf8'), addr)
