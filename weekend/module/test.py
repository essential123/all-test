# 1.编写一个统计指定文件类型的脚本工具
#     输入指定类型的文件后缀
#        eg:.txt
#     并给出一个具体路径 之后统计该类型文件在该文件下的个数
#     ps:简单实现即可 无需优化
import os

# import os
# # 获取指定路径
# target_path = input('请输入目录路径>>:').strip()
# # 获取目标后缀
# target_postfix = input('请输入目标后缀>>:').strip()
# # 获取指定路径下的所有文件名称
# file_name_list = os.listdir(target_path)
# print(file_name_list)
# count = 0
# # 循环获取每一个文件名，然后判断是否以target_postfix结尾
# for file_name in file_name_list:
#     if file_name.endswith(target_postfix):
#         count += 1
# print(f'目录{target_path}下后缀名为{target_postfix}的文件数目有{count}')


# json模块实操.涉及到用户数据的存储 可以单用户单文件
# import json
# import os
# base_dir =os.path.dirname(__file__)
# db_path = os.path.join(base_dir,'db')
# if not os.path.exists('db'):
#     os.mkdir(r'db')
# info_list = os.listdir('db')
# username = input('请输入用户名>>:').strip()
# file_path = os.path.join(db_path, '%s' % username)
# if username in info_list:
#     with open(file_path,'r',encoding='utf8')as f:
#         data = json.load(f)
#         print(data)
# else:
#     password = input('请输入密码>>:').strip()
#     user_dict={
#         'username':username,
#         'password':password,
#         'balance':15000,
#         'shop_car':[]
#     }
#     with open(file_path,'a',encoding='utf8')as f:
#         json.dump(user_dict,f)


# # 2.尝试单文件多用户(一行一个)是否可实现 哪个更方便
# import json
# import os
# base_dir =os.path.dirname(__file__)
# db_path = os.path.join(base_dir,'db')
# if not os.path.exists('db.txt'):
#     with open('db.txt','a',encoding='utf8'):
#         pass
# username = input('请输入用户名>>:').strip()
# with open('db.txt','r',encoding='utf8')as f:
#     # data = json.load(f)
#     data = f.read()
#     if username in data:
#         print('用户名已存在')
#     else:
#         password = input('请输入密码>>:').strip()
#         user_dict={
#             'username':username,
#             'password':password,
#             'balance':15000,
#             'shop_car':[]
#         }
#
#         with open('db.txt','a',encoding='utf8')as f:
#             json.dump(user_dict,f)
#         with open("db.txt", 'a') as f:
#             f.write('\n')

# 3.编程小练习
# 	有一个目录文件下面有一堆文本文件
#     	eg:
#     		db目录
#             J老师视频合集
#             R老师视频合集
#             C老师视频合集
#             B老师视频合集
# 	文件内容自定义即可 要求循环打印出db目录下所有的文件名称让用户选择
#  	用户选择哪个文件就自动打开该文件并展示内容
#  	涉及到文件路径全部使用代码自动生成 不准直接拷贝当前计算机固定路径
# import os
# base_url = os.path.dirname(__file__)    # module文件目录绝对路径
# db_path = os.path.join(base_url,'db')
# file_list = os.listdir(db_path)
# while True:
#     for i in file_list:
#         print(i)
#     choice = input('请输入您要打开的文件名>>:').strip()
#     file_path = os.path.join(db_path,choice)
#     with open(file_path,'r',encoding='utf8')as f:
#         data = f.read()
#         print(data)
#
