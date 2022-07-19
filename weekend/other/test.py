# import time
# class deco:
#     def __init__(self,index):
#         self._index = index
#     def __call__(self,*args,**kwargs):
#         start = time.time()
#         self._index(*args,**kwargs)
#         end= time.time()
#         print(f'函数运行的时间为{end-start}')
#
# @deco
# def add(*args):
#     time.sleep(1)
#     print(sum(args))
#
# add(1,2,3,4,5)


# def a():
#     print('hello world')
#
#
# a()  # hello world
# print(callable(a))  # True 发现函数a调用过后，是个可调用对象
#
#
# class B:
#     pass
# print(callable(B))  # True 类A是个可调用对象
# b = B()
# print(callable(b))  # False 实例对象不可调用
#
# # 类的__call__这个方法可以让实例对象变得可调用，能够像函数一样加小括号进行调用
#
# class B:
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         print('hello world')
# b=B()
# print(callable(b))  # True  实例对象变得可调用


# class deco:
#     def __init__(self,name,age):
#         self.name =name
#         self._age = age
#     def __call__(self, *args, **kwargs):
#         pass
#
# a = deco('jason',18)
# print(a._age)

# l1 = [11, 23, 32, 45, 65, 78, 90, 123, 432, 467, 567, 687, 765, 876, 999, 1131, 1232]
# # target_num = input('请输入你要查找的数字>>:').strip()
# count=0
# def get_num(l1,target_num):
#     global count
#     index = len(l1)//2
#     if target_num > l1[index]:
#         count+=1
#         get_num(l1[index+1:],target_num)
#     elif target_num < l1[index]:
#         count += 1
#         get_num(l1[:index],target_num)
#     else:
#         print('找到啦')
#
#
# get_num(l1,45)














