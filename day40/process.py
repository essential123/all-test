# from multiprocessing import Process
# money = 100
#
# def task():
#     global money
#     money =666
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     print(money)



# from multiprocessing import Process
# import time
# def task(name):
#     print(f'{name}正在运行')
#     time.sleep(1)
#     print(f'{name}运行结束')
# if __name__ == '__main__':
#     p = Process(target=task, args=('jason',))  # 创建一个进程对象
#     p.start()  # 告诉操作系统创建一个进程(异步操作)
#     # task('jason')  # 提交一个task任务，普通的函数调用（同步操作）
#     print('主进程')


# from multiprocessing import Process
# import time
# def task(name):
#     print(f'{name}正在运行')
#     time.sleep(5)
#     print(f'{name}运行结束')
# if __name__ == '__main__':
#     p = Process(target=task, args=('jason',))  # 创建一个进程对象
#     p.start()  # 告诉操作系统创建一个进程(异步操作)
#     p.join()
#     print('主进程')






# from multiprocessing import Process
# import time
# def task(name, n):
#     print(f'{name}正在运行')
#     time.sleep(n)
#     print(f'{name}运行结束')
# if __name__ == '__main__':
#     p1 = Process(target=task, args=('tom', 1))  # args就是通过元组的形式给函数传参
#     p2 = Process(target=task, args=('kevin', 2))  # 也可以通过kwargs={'name':'jason', 'n':1} 太麻烦 没必要
#     p3 = Process(target=task, args=('jerry', 3))
#     start_time = time.time()
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     end_time = time.time() - start_time
#     print('总耗时:%s' % end_time)
#     print('主进程')

# from multiprocessing import Process
# money = 100
# def task():
#     global money
#     money = 666
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     print(money)



# from multiprocessing import Process
# money = 100
# def task():
#     global money
#     money = 666
#     print('子进程打印的money', money)
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     p.join()
#     print('父进程打印的money', money)

# from multiprocessing import Queue
# # 1.创建队列对象
# q = Queue(3)  # 括号内指定队列可以容纳的数据个数 默认:2147483647
# # 2.往队列添加数据
# q.put(111)
# q.put(222)
# q.put(333)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(False))




# from multiprocessing import Queue, Process
#
#
# def procedure(q):
#     q.put('子进程procedure往队里中添加了数据')
#
#
# def consumer(q):
#     print('子进程的consumer从队列中获取数据', q.get())
#
#
# if __name__ == '__main__':
#     q = Queue()  # 在主进程中产生q对象 确保所有的子进程使用的是相同的q
#     p1 = Process(target=procedure, args=(q,))
#     # 产生一个进程对象，对象.start方法就可以变成一个进程，单独开辟了内存空间，并且会自动调用（target后面的procedure）函数
#     p2 = Process(target=consumer, args=(q,))
#     p1.start()
#     p2.start()
#     print('主进程')

# from multiprocessing import Process
#
# import time
# import os
#
# def task(name,age):
#     print("子进程的id号: %s" % os.getpid())   # 子进程pid   # os.getpid()获取当前id号
#     print("父进程的id号：%s" % os.getppid())   # 主进程pid
#
# if __name__ == '__main__':
#     p = Process(target=task, kwargs={'name': 'qq', 'age': 11})  # Process——>子进程
#     p.start()
#     print(p.pid)   # pid——>是子进程的pid
#     print("main里的主进程的id号：%s" % os.getpid())  # 主进程pid
#     print("main里面的父进程的id号：%s" % os.getppid())      # pycharm的pid

# from multiprocessing import current_process,Process
# import os
# def task():
#     print(os.getpid())
# if __name__ == '__main__':
#     p1 = Process(target=task)
#     p1.start()


# from multiprocessing import Process
# import time
#
# def task(name):
#     print('大内总管:%s存活' % name)
#     time.sleep(3)
#     print('大内总管:%s嗝屁' % name)
#
# if __name__ == '__main__':
#     p = Process(target=task, args=('tom',))
#     p.daemon = True  # 将子进程设置为守护进程:主进程代码结束 子进程立刻结束
#     p.start()
#     print('天子寿终正寝!!!')

import json
import time
import random
from multiprocessing import Process

# 查票
def search(i):
    # 文件操作读取票数
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print('用户%s查询余票：%s' % (i, dic.get('ticket_num')))

# 买票
def buy(i):
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    time.sleep(random.randint(1,3))
    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1
        with open('data', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
            print(('用户%s购买成功' % i))
    else:
        print('用户%s很倒霉 没有抢到票' % i)

def run(i):
    search(i)
    buy(i)

if __name__ == '__main__':
    for i in range(1,11):
       p=Process(target=run,args=(i,))
       p.start()












