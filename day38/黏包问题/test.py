# import struct
#
# info = '艺画开天《灵笼》获湖北省广播电视文艺奖'
# print(len(info))  # 19 数据原来长度
# res = struct.pack('i', len(info))  # 将数据原本的长度打包
# print(len(res))  # 4 ,用i打包之后的长度固定4
#
# ret = struct.unpack('i',res)
# print(ret[0])  # 19，这里的ret是一个元组（19,）

# import struct
# file_size = 12345678900000
# res = struct.pack('i',file_size)
# print(len(res))
# ret = struct.unpack('i',res)
# print(ret[0])




