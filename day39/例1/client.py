import socket
client = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1',8080)
client.sendto('你好呀，我是客户端'.encode('utf8'),addr)
msg, addr = client.recvfrom(1024)
print('msg>>:',msg.decode('utf8'))
print('addr>>:',addr)