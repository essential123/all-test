# def deco1(func1):  # func1=函数wrapper2的内存地址
#     print('加载了deco1')
#
#     def wrapper1(*args, **kwargs):
#         res1 = func1(*args, **kwargs)
#         print('执行了wrapper1')
#         return res1
#
#     return wrapper1
#
#
# def deco2(func2):  # func2=函数wrapper3的内存地址
#     print('加载了deco2')
#
#     def wrapper2(*args, **kwargs):
#         res2 = func2(*args, **kwargs)
#         print('执行了wrapper2')
#         return res2
#
#     return wrapper2
#
#
# def deco3(func3):  # func3 = 最原始那个index函数的内存地址
#     print('加载了outter3')
#
#     def wrapper3(*args, **kwargs):
#         res3 = func3(*args, **kwargs)
#         print('执行了wrapper3')
#         return res3
#
#     return wrapper3
#
#     # index=函数wrapper1的内存地址
#
#
# @deco1  # deco1(函数wrapper2的内存地址)->函数wrapper1的内存地址
# @deco2  # deco2(函数wrapper3的内存地址)->函数wrapper2的内存地址
# @deco3  # deco3(最原始那个index函数的内存地址)->函数wrapper3的内存地址
# # 加载顺序是自下而上的
#
# def index():
#     print('from index')
#     return 123
#
#
# res = index()
# print(res)
