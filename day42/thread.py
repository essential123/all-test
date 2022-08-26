# from threading import Thread,Lock
# import time
# money = 100
# mutex =Lock()
# def task():
#     mutex.acquire()
#     global money
#     tmp = money
#     time.sleep(0.1)
#     money =tmp - 1
#     mutex.release()
# t_list = []
# for i in range(100):
#     t = Thread(target=task)
#     t.start()
#     t_list.append(t)
# for t in t_list:
#     t.join()
# print(money)

# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# from threading import current_thread
# import time
#
# pool = ThreadPoolExecutor(5)  # 固定产生5个线程
#
#
# def task():
#     print(current_thread().name)
#     time.sleep(1)
#
#
# def func(*args, **kwargs):
#     print('func', args, kwargs)
#
#
# for i in range(100):
#     # res = pool.submit(task) # 朝池子中提交任务（异步）
#     # print(res.result()) # 同步，不能直接在这里获取结果
#     pool.submit(task).add_done_callback(func)

#
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# from threading import current_thread
# import time
#
# pool = ThreadPoolExecutor(5)  # 固定产生5个线程
#
#
# def task():
#     print(current_thread().name)
#     time.sleep(1)
#
#
# def func(*args, **kwargs):
#     print('func', args, kwargs)
#
#
# for i in range(100):
#     # res = pool.submit(task) # 朝池子中提交任务（异步）
#     # print(res.result()) # 同步，不能直接在这里获取结果
#     pool.submit(task).add_done_callback(func)


# from multiprocessing import Process
# import os
# import time
# def work():
#     res =1
#     for i in range(1,100000):
#         res *= i
# if __name__ == '__main__':
#     print(os.cpu_count()) # 计算cpu个数
#     start_time = time.time()
#     p_list = []
#     for i in range(4): # 一次性创建4个进程
#         p = Process(target=work)
#         p.start()
#         p_list.append(p)
#     for p in p_list: # 确保所有的进程全都运行完毕
#         p.join()
#     print('总耗时:%s' %(time.time()-start_time)) # 总耗时:8.251912832260132





# from threading import Thread
# import os
# import time
# def work():
#     res =1
#     for i in range(1,100000):
#         res *= i
# if __name__ == '__main__':
#     print(os.cpu_count()) # 计算cpu个数
#     start_time = time.time()
#     t_list=[]
#     for i in range(4):
#         t = Thread(target=work)
#         t.start()
#         t_list.append(t)
#     for t in t_list:
#         t.join()
#     print('总耗时:%s' %(time.time()-start_time)) # 获取总耗时:15.50655484199524

#
#
# from multiprocessing import Process
# import os
# import time
# def work():
#     time.sleep(2)
# if __name__ == '__main__':
#     print(os.cpu_count()) # 计算cpu个数
#     start_time = time.time()
#     p_list = []
#     for i in range(10): # 一次性创建4个进程
#         p = Process(target=work)
#         p.start()
#         p_list.append(p)
#     for p in p_list: # 确保所有的进程全都运行完毕
#         p.join()
#     print('总耗时:%s' %(time.time()-start_time)) # 总耗时:4.0351951122283936
#
#
#
#
#
# from threading import Thread
# import os
# import time
# def work():
#     time.sleep(2)
# if __name__ == '__main__':
#     print(os.cpu_count()) # 计算cpu个数
#     start_time = time.time()
#     t_list=[]
#     for i in range(10):
#         t = Thread(target=work)
#         t.start()
#         t_list.append(t)
#     for t in t_list:
#         t.join()
#     print('总耗时:%s' %(time.time()-start_time)) # 获取总耗时:2.018876791000366


# from threading import Thread, Lock
# import time
#
# mutexA = Lock()  # 类名加括号每执行一次就会产生一个新的对象
# mutexB = Lock()  # 类名加括号每执行一次就会产生一个新的对象
#
#
# class MyThread(Thread):
#     def run(self):
#         self.func1()
#         self.func2()
#
#     def func1(self):
#         mutexA.acquire()
#         print(f'{self.name}抢到了A锁')
#         mutexB.acquire()
#         print(f'{self.name}抢到了B锁')
#         mutexB.release()
#         print(f'{self.name}释放了B锁')
#         mutexA.release()
#         print(f'{self.name}释放了A锁')
#
#     def func2(self):
#         mutexB.acquire()
#         print(f'{self.name}抢到了B锁')
#         time.sleep(1)
#         mutexA.acquire()
#         print(f'{self.name}抢到了A锁')
#         mutexA.release()
#         print(f'{self.name}释放了A锁')
#         mutexB.release()
#         print(f'{self.name}释放了B锁')
#
#
# for i in range(10):
#     t = MyThread()
#     t.start()


#
# from threading import Thread,Lock,Semaphore
# import time
# import random
# sp = Semaphore(5) # 一次产生多把锁
# class MyThread(Thread):
#     def run(self):
#         sp.acquire()
#         print(self.name)
#         time.sleep(random.randint(1, 3))
#         sp.release()
# for i in range(20):
#     t=MyThread()
#     t.start()

# from threading import Thread, Event
# import time
#
# event = Event()  # 类似于造了一个红绿灯
#
#
# def light():
#     print('红灯亮着的 所有人都不能动')
#     time.sleep(2)
#     print('绿灯亮了 油门踩到底 给我冲!!!')
#     event.set()
#
#
# def car(name):
#     print('%s正在等红灯' % name)
#     event.wait()
#     print('%s加油门 飙车了' % name)
#
#
# t = Thread(target=light)
# t.start()
# for i in range(10):
#     t = Thread(target=car, args=('熊猫PRO%s' % i,))
#     t.start()


### 进程池和线程池


"""
多进程 多线程
	在实际应用中是不是可以无限制的开进程和线程
	肯定不可以!!! 会造成内存溢出受限于硬件水平
我们在开设多进程或者多线程的时候 还需要考虑硬件的承受范围

池
	降低程序的执行效率 保证计算机硬件的安全
进程池
	提前创建好固定个数的进程供程序使用 后续不会再创建
线程池
	提前创建好固定个数的线程供程序使用 后续不会再创建
"""
# submit(函数名,实参1,实参2,...)
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import current_thread
import os
import time

# pool = ThreadPoolExecutor(5)  # 固定产生五个线程
pool = ProcessPoolExecutor(5)  # 固定产生五个线程


def task(n):
    # print(current_thread().name)
    print(os.getpid())
    # print(n)
    time.sleep(1)
    return '返回的结果'


def func(*args, **kwargs):
    print('func', args, kwargs)
    print(args[0].result())


if __name__ == '__main__':
    for i in range(5):
        # res = pool.submit(task,123)  # 朝池子中提交任务(异步)
        # print(res.result())  # 同步
        # pool.submit(task, 123).add_done_callback(func)
        """异步回调:异步任务执行完成后有结果就会自动触发该机制"""
        pool.submit(task, 123).add_done_callback(func)


###