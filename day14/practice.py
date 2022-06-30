# import os
#
# file_name = 'userinfo.txt'
#
#
# def register():
#     all_user_info=[]
#     username = input('请输入您的用户名>>:').strip()
#     password = input('请输入您的密码>>:').strip()
#     if username and password:
#         info_data = username + ',' + password + '\n'
#         with open(file_name,'rb') as f:
#             file_info=f.readlines()   # ['第一行\n','aaa,111\n']
#             for line in file_info:
#                 all_user_info.append(line.decode().strip('\n'))
#                 if info_data not in all_user_info:
#                     with open(file_name, 'ab') as f:
#                         new_info_data=info_data.encode('utf-8')
#                         f.write(new_info_data)
#                         print('注册成功')
#     else:
#         print('用户名不存在')
# def login():
#     all_user_info = []
#     username = input('请输入您的用户名>>:').strip()
#     password = input('请输入您的密码>>:').strip()
#     with open(file_name, 'rb') as f:
#         if username and password:
#             info_data = username + ',' + password + '\n'
#         file_info = f.readlines()  # ['第一行\n','aaa,111\n']
#         for line in file_info:
#             all_user_info.append(line.rstrip())
#             if info_data in all_user_info:
#                 print(f'{username}登录成功')
#                 break
#             else:
#                 print('用户名或者密码错误')
#                 break
#         else:
#             print('用户名不存在')
#
#
#
# def out():
#     exit()
#
#
# command_dict = {
#     '1': ['注册', register],
#     '2': ['登录', login],
#     '3': ['退出', out]
# }
#
#
# def main_body():
#     while True:
#         for choice, command in command_dict.items():
#             print(choice, command_dict[choice][0])
#         choice = input('请输入您的指令>>:').strip()
#         if choice in command_dict:
#             command_dict[choice][1]()
#         else:
#             print('输入有误，请重新输入')
#
#
# if __name__ == '__main__':
#
#     if os.path.exists(file_name):
#         pass
#     else:
#         with open(file_name, 'a', encoding='utf-8') as f:
#             pass
#         # os.mknod(file_name)
#
#     main_body()
