# import socket
# server = socket.socket()
# server.bind(('127.0.0.1',8080))
# server.listen(5)
# sock, addr=server.accept()
# data=sock.recv(1024)
# print(data)
# sock.send(b'HTTP\1.1 OK 200 \r\n\r\n hello baby')

# print('jason'.join('ss'))

from functools import reduce
l2 = [1, 2, 3]
res = reduce(lambda x, y: x + y, l2, 100)
print(res)