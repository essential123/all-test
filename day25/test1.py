import os, sys, datetime, json
# import time
# print(time.time())

#
# import time
# import datetime
# res1 = datetime.date.today() # 2022-07-15
# res = datetime.datetime.today() # 2022-07-15 09:53:46.004000
#
# print(res.year)
# print(res.month)
# print(res.weekday())
# print(res.isoweekday())


# import datetime

# print(datetime.date.today())   # 2022-07-15
# print(datetime.datetime.today())  # 2022-07-15 15:52:41.167516

# print(res.year) # 2022
# print(res.month) # 7
# print(res.weekday()) # 4
# print(res.isoweekday()) # 5

# print('指定日期：',datetime.datetime(2017, 5, 23, 12, 20)) # 指定日期： 2017-05-23 12:20:00
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

# import os

# print(os.mkdir(r'ddd'))
# print(os.makedirs(r'ccc'))
# print(os.makedirs(r'ccc\ddd'))
# print(os.makedirs(r'ddd\ccc'))
# print(os.makedirs(r'eee'))
# print(os.makedirs(r'eee\bbb\ccc'))

# print(os.rmdir(r'eee/bbb/ccc'))
# print(os.removedirs(r'eee/bbb'))

# os.mkdir(r'ccc') # 只能创建单级目录（文件夹）
# os.mkdir(r'aaa\bbb\ccc') # 只能创建单级目录（文件夹）
# os.removedirs(r'ccc') # 针对有数据的目录也无法删除
# print(os.makedirs(r'ccc\ddd'))
# os.removedirs(r'aaa/bbb/ccc') # 针对有数据的目录也无法删除

# print(os.listdir('D:/'))


# str = 'd\nddddd'
# str1 = r'd\nddddd'
# print(str)
# print(str1)

# print(os.getcwd())
# os.chdir(r'..')
# print(os.getcwd())
# import os
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# import os
# absolute_path = os.path.dirname(os.path.dirname(__file__))
# relative_path = r'day25/test'
# res=os.path.join(absolute_path,relative_path)
# print(res)
# print(os.path.exists('../day25'))

import time

# print(time.time()) # 时间戳:1657949304.8721797
#
#
# # 按照某种格式显示时间，用于展示时间
# print(time.strftime("%Y-%m-%d %H:%M:%S %p")) # 2022-07-16 13:28:24 PM
# print(time.strftime("%Y-%m-%d %X %p")) # 2022-07-16 13:28:24 PM
#
#

# # 获取当前时间的某一部分


# print(time.strptime('1988-03-03 11:11:11','%Y-%m-%d %H:%M:%S'))
# time.struct_time(tm_year=1988, tm_mon=3, tm_mday=3, tm_hour=11, tm_min=11, tm_sec=11, tm_wday=3, tm_yday=63, tm_isdst=-1)


# import sys
#
# print(sys.argv)
# args=sys.argv
# for i in range(1,len(sys.argv)):
#     print(f"i am {sys.argv[i]}")


# absolute_path = r'D:\pythonProject\ccc\ddd'
# relative_path = 'a.txt'
# res = os.path.join(absolute_path, relative_path)
# print(res)

# print(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
# path_file = os.path.join(BASE_DIR, 'db')
# print(path_file)
#
# data = {'name': 'jason', 'pwd': 123}
# with open('a.txt', 'a', encoding='utf-8') as f:
#     json.dumps(data)


# info1 = {'name': 'tom', 'age': 18}
# res1 = json.dumps(info1)  # 序列化    将其他数据类型转换 成json格式字符串
# print(res1, type(res1))  # {"name": "tom", "age": 18} <class 'str'>
#
# res2 = json.loads(res1)  # 反序列化   将json格式字符串转换成对应编程语言中的数据类型
# print(res2, type(res2))  # {'name': 'tom', 'age': 18} <class 'dict'>

# info = {'name': 'tom', 'age': 18}
# with open(r'b.txt','a',encoding='utf8')as f:
#     json.dump(info,f)
# with open(r'b.txt','r',encoding='utf8')as f:
#     data=json.load(f) # load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
# print(data,type(data)) # {'name': 'tom', 'age': 18} <class 'dict'>
#
