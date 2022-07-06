# 1.尝试编写有参函数将多种用户验证方式整合到其中
#     直接获取用户数据比对
#     数据来源于列表
#     数据来源于文件

# def outter(db_type):
#     def deco(func):
#         def wrapper(*args, **kwargs):
#             username = input('请输入你都名字>>:').strip()
#             password = input('请输入你的密码>>:').strip()
#             if db_type == 'file':
#                 print('基于文件的验证')
#                 if username == 'xxx' and password == '123':
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('账号或者密码错误')
#             elif db_type == 'mysql':
#                 print('基于mysql的验证')
#             else:
#                 print('不支持db_type')
#         return wrapper
#     return deco
#
# @outter(db_type='file')
# def index():
#     print('from index')

# @outter(db_type='list')
# def index():
#     print('from index')
# index()

# list = ['A','B','C','D','E']
# def recursion(age):
#     age = int(age)
#     if age == 18:
#         age -= 2
#         recursion(age)
#
# res=recursion(18)
# print(res)



# 2.尝试编写递归函数
#     推导指定某个人的正确年龄
#       eg: A B C D E 已知E是18 求A是多少

list = ['A','B','C','D','E']

def recursion(age):
    age = int(age)
    if len(list)-1==0:
        print(age)
        return
    else :
        age +=2
        list.pop()
        recursion(age)

recursion(18)









