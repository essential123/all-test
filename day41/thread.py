# # from threading import Thread
# # import time
# # def task(name):
# #     print(f'{name}正在运行')
# #     time.sleep(3)
# #     print(f'{name}运行结束')
# # if __name__ == '__main__':
# #     t = Thread(target=task, args=('tom',))
# #     t.start()
# #     print('主线程')
#
from threading import Thread
import time
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name =name
    def run(self):
        print(f'{self.name}正在运行')
        time.sleep(3)
        print(f'{self.name}运行结束')

obj = MyThread('tom')
obj.start()
print('主线程')


# # from threading import Thread
# # money =10000
# # def func():
# #     global money
# #     money =666
# #
# # func()
# # print(money)
#
# from threading import Thread
# money = 10000
# def func():
#     global money
#     money = 666
# t = Thread(target=func)
# t.start()
# t.join()
# print(money)
#

# from threading import Thread,current_thread,active_count
# import os
# import time
#
# def task():
#     print('子线程运行task函数')
#     time.sleep(5)
#     print('子线程运行task结束')
#     print('子线程名',current_thread().name)
# if __name__ == '__main__':
#     print('主线程',os.getpid())
#     for i in range(4):
#         t= Thread(target=task,)
#         t.start()
#     print('当前进程下存活的线程数>>:',active_count)

# from threading import Thread
# import time
#
# def task():
#     print('子线程运行task')
#     time.sleep(3)
#     print('子线程结束task')
#
# t = Thread(target=task())
# t.daemon= True
# t.start()
# print('主进程')


# 主线程等到子线程运行结束之后再运行
# from threading import Thread
# import time
#
# def task():
#     print('正在执行')
#     time.sleep(3)
#     print('运行结束')
#
# t = Thread(target=task)
# t.start()
# t.join()
# print('主线程')


from threading import Thread,current_thread
import time
import os

def task():
    print('子进程运行task函数')
    time.sleep(2)
    print('子进程运行task函数结束')
    print('子线程',os.getpid())
    print('子线程名>>:',current_thread().name)

if __name__ == '__main__':
    print('主线程',os.getpid())
    for i in range(2):
        t=Thread(target=task,)
        t.start()








