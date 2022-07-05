# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# l1 = [1, 2, 3, 4, 5]
# func(*l1)
# # ([1, 2, 3, 4, 5],)
# # {}

# def func(*args,**kwargs):
#     print(kwargs)
#     # pass
# d1 = {'username':'jason','pwd':123}
# func(**d1)

# def func(a,b,*args,c):
#     print(a,b,*args,c)
#     print(type(a),type(c))
# func(1,2,3,c=666)

# def func(*args,**kwargs):
#     print(args,kwargs)
# func()  # () {}
# func([1,2,3,4,5])  # ([1, 2, 3, 4, 5],) {}

# def func(*args, **kwargs):
#     print(args,kwargs)
#
# func()  # ()  {}
# func([1, 2, 3, 4, 5, 6])  # ([1, 2, 3, 4, 5, 6],) {}
# l1 = [1, 2, 3, 4, 5, 6]
# func(l1[0], l1[1], l1[2], l1[3], l1[4], l1[5])  # (1,2,3,4,5,6) {}
#
# func(*l1)  # (1, 2, 3, 4, 5, 6) {}
#
# d1 = {'username': 'jason', 'pwd': 123}
# func(**d1)  # ()  {'username': 'jason', 'pwd': 123}
# func(username='jason', pwd=123)  # ()  {'username': 'jason', 'pwd': 123}

# '''需要形参在传实参的时候 必须按照关键字参数才可以'''
# # 在形参*args的后面
# def func(a, b, *args, c):
#     print(a, b, args, c)
# # func(1,2,3,4,5,6,7)  # 报错
# func(1, 2, 3, 4, 5, 6, c=666) # 1 2 (3, 4, 5, 6) 666
# # 如果形参中还有**kwargs 那必须在它的前面
# def func(a,b,*args,c,**kwargs):
#     print(a,b,args,c,kwargs)
# func(1,2,3,4,5,6,c=123,name='jason') # 1 2 (3, 4, 5, 6) 123 {'name': 'jason'}

x = 1


# def func1():
#     x = 2
#     def func2():
#         x = 3
#         def func3():
#             # print(x)  # 特例
#             x = 4
#             print(x)
#         func3()
#     func2()
# func1()


# money = 999
#
# def func():
#     global money  # 声明 局部名称空间中的money操作的是全局的money
#     money = 1000
#     print(money) # 1000
# func()
# print(money) # 1000

# 正常情况下,局部名称空间里面出现新的名字会在局部名称空间中存储,但是有时候需要在局部名称空间中修改全局名称空间的名字



# l1 = [1, 2, 3, 4, 5]
# s = '$jason$'
#
# def func():
#     global s
#     res = s.strip('$')
#     print(res) # s = 'jason
#     l1.append(113123)
#     l1.append(666)
#
# func()
# print(l1) # [1, 2, 3, 4, 5, 113123, 666]
"""
局部修改全局名称空间中不可变类型的数据 需要使用关键字global声明
如果是可变类型 则无需关键字声明
"""


# def func1():
#     x = 1
#     l1 = [1,2]
#     def func2():
#         # nonlocal x
#         x = 999
#         l1.append(666)
#     func2()
#     print(x)
#     print(l1)
# func1()
# nonlocal 在内存局部名称空间修改外层局部名称空间中的不可变类型


#
# def func1():
#     x = 1
#     l1 = [1,2]
#     def func2():
#         nonlocal x
#         x = 999
#         l1.append(666)  # [1, 2, 666]
#     func2()
#     print(x) # 999
#     print(l1)  # [1, 2, 666]
# func1()
#
# # nonlocal 在内存局部名称空间修改外层局部名称空间中的不可变类型


# # 1.函数名也可以被用来多次赋值(函数名与变量名使用一致)
# def func():
#     print('from func')
# name = func
# name()

# # 2.函数名还可以当做函数的实参
# def func():
#     print('from func')
#
# def index(a):
#     print(a)   # func的内存地址, func()--->from func
#     a()
#
# index(func)

# # 3.函数名还可以当做函数的返回值
# def func():
#     print('from func')
# def index():
#     return func
# res = index()  # func
# print(res)  # func的内存地址 <function func at 0x0000000000D45280>
# res()  # func()--->from func

# # 4.函数名还可以当做容器类型里面的数据值
# def func():
#     print('from func')
# l1 = [1,2,3,4,func]
# print(l1) # [1,2,3,4,func的内存地址]
# l1[-1]()  # func（） func()--->from func


# 统计目录下所有文件的大小
# import os
# sum_size = 0
# for file in os.listdir('.'):
#     if os.path.isfile(file):
#         sum_size +=os.path.getsize(file)
# print(sum_size)

import os
print(os.getcwd())


























































































































































































































