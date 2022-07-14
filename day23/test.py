# import time
#
#
# def outter(func_name):
#     def inner(*args,**kwargs):
#         start = time.time()
#         time.sleep(1)
#         res = func_name(*args,**kwargs)
#         stop = time.time()
#         print('执行函数:%s,执行函数时间：%s' %(func_name.__name__,stop-start))
#         return res
#     return inner
#
# @outter
# def index():
#     print('from index')
# index()



# print(__name__)














