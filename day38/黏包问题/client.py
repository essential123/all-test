# import socket
# # 1.产生一个socket对象
# client = socket.socket()
# # 2.连接服务端(拼接服务端的ip和port)
# client.connect(('127.0.0.1', 8080))
# # 3.数据交互
# while True:
#     msg = input('请输入发送给服务端的消息>>:').strip()
#     if len(msg) == 0: continue
#     client.send(msg.encode('utf8'))  # 朝服务端发送数据
#     data = client.recv(1024)  # 接收服务端发送的数据
#     print(data.decode('utf8'))


# import socket
# # 1.产生一个socket对象
# client = socket.socket()
# # 2.连接服务端(拼接服务端的ip和port)
# client.connect(('127.0.0.1', 8080))
# client.send(b'tom')
# client.send(b'kevin')
# client.send(b'tony')
import struct
import json
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8080))
while True:
    # 先接收长度为4的报头数据
    handler_len = client.recv(4)
    # 根据报头解包出的字典的长度
    dict_len = struct.unpack('i', handler_len)[0]
    # 直接接收字典数据
    dict_data = client.recv(dict_len)
    # 解码并且反序列化成字典
    # json.loads() # 能够识别括号内是一个json字符串还是bytes类型字符串，如果是bytes类型的字符串会自动先解码在反序列化
    real_dict = json.loads(dict_data)
    # 从数据字典获取真实数据的各项信息
    total_size = real_dict.get('file_size')
    file_size = 0
    with open(r'%s' % real_dict.get('file_name'), 'wb') as f:
        while file_size < total_size:
            data = client.recv(1024)
            f.write(data)
            file_size += len(data)
        print('文件接收完毕')
        break