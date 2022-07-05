# def outter(func):
#     def inner(*args,**kwargs):
#         username = input('请输入账号>>:').strip()
#         password = input('请输入密码>>:').strip()
#         if username == 'jason' and password == '123':
#             print('登录成功')
#             res= func(*args,**kwargs)
#             return res
#         else:
#             print('账号或者密码错误')
#     return inner
#
# @outter
# def index():
#     print(123)
#     return 'index执行成功'
# res=index()
# print(res)

