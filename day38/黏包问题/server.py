# import socket
# # 1.创建一个socket对象
# server = socket.socket()  # 括号内什么都不写 默认就是基于网络的TCP套接字
# # 2.绑定一个固定的地址(ip\port)
# server.bind(('127.0.0.1', 8080))  # 127.0.0.1本地回环地址(只允许自己的机器访问)
# # 3.半连接池
# server.listen(5)
# while True:
#     # 4.开业 等待接客
#     sock, address = server.accept()
#     print(sock, address)  # sock是双向通道 address是客户端地址
#     # 5.数据交互
#     while True:
#         try:
#             data = sock.recv(1024)  # 接收客户端发送的数据 1024bytes
#             print(data.decode('utf8'))
#             msg = input('请输入发送给客户端的消息>>:').strip()
#             sock.send(msg.encode('utf8'))  # 朝客户端发送数据
#         except ConnectionResetError:
#             sock.close()
#             break

# import socket
# # 1.创建一个socket对象
# server = socket.socket()  # 括号内什么都不写 默认就是基于网络的TCP套接字
# # 2.绑定一个固定的地址(ip\port)
# server.bind(('127.0.0.1', 8080))  # 127.0.0.1本地回环地址(只允许自己的机器访问)
# server.listen(5)
# sock, address = server.accept()
# data = sock.recv(1024)
# print(data)
# data = sock.recv(1024)
# print(data)
# data = sock.recv(1024)
# print(data)
import os
import socket
import struct
import json
# 1.创建一个socket对象
server = socket.socket()
# 2.绑定一个固定的地址(ip\port)
server.bind(('127.0.0.1',8080))
# 3.半连接池
server.listen(5)
while True:
    sock,addr = server.accept()
    while True:
        # 先构造数据文件的字典
        file_dict = {
            'file_name':'嗨咯喂.mp3',
            'file_size': os.path.getsize(r'../嗨咯喂 - JelloRio李佳隆.m4a'),
            'file_desc':'内容很精彩',
            'file_root': 'jzb'
        }
        # 将字典打包成固定长度的数据(需要先转成bytes类型)
        dict_json = json.dumps(file_dict)
        file_bytes_dict = len(dict_json.encode('utf8'))
        dict_len = struct.pack('i',file_bytes_dict)
        # 发送固定长度的字典报头
        sock.send(dict_len)
        # 发送真实字典数据
        sock.send(dict_json.encode('utf8'))
        # 发送真实数据
        with open(r'../嗨咯喂 - JelloRio李佳隆.m4a','rb') as f:
            for line in f:
                sock.send(line)
        break













