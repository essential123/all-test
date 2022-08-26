import socket

server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))
msg,addr=server.recvfrom(1024)
print('msg>>:',msg.decode('utf8'))
print('addr>>:',addr)
server.sendto('你好呀，我是服务端'.encode('utf8'),addr)