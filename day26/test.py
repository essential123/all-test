# import os
#
# base_path = os.path.dirname(__file__)
# db_path = os.path.join(base_path,'db')
# db_file_list = os.listdir(db_path)
# print(db_file_list)
# while True:
#     for k,v in enumerate(db_file_list,start=1):
#         print(k,v)
#     choice = input('请输入你想要打开的文件编号>>:')
#     if not choice.isdigit():
#         print('输入有误，请重新输入编号')
#         continue
#     choice = int(choice)
#     if not choice in range(1,len(db_file_list)+1):
#         print('数字超出范围')
#         continue
#     file_name = db_file_list[choice-1]
#     file_path = os.path.join(db_path,file_name)
#     with open(file_path,'r',encoding='utf8')as f:
#         print(f.read())