# import socket
# client = socket.socket(type=socket.SOCK_DGRAM)
# addr = ('127.0.0.1', 8080)
# while True:
#     send_data = input('请输入要发给客户端的信息>>:').strip()
#     client.sendto(('来自客户端1的消息：%s' % send_data).encode('utf8'), addr)
#     msg, addr = client.recvfrom(1024)
#     print('msg>>:', msg.decode('utf8'))
#     print('addr>>:', addr)


import socket
client = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1', 8080)
send_data = input('请输入要发给客户端的信息>>:').strip()
client.sendto(('来自客户端1的消息：%s' % send_data).encode('utf8'), addr)
client.sendto(('来自客户端1的消息：%s' % send_data).encode('utf8'), addr)
client.sendto(('来自客户端1的消息：%s' % send_data).encode('utf8'), addr)
