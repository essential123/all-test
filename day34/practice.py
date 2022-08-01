# 加载配置文件：获取配置文件中的所有大写配置，小写直接忽略,组成字典
# import settings
# print(dir(settings))
# ['AGE', 'INFO', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'desc', 'name']
# new_dict = {}
# for i in dir(settings):
#     if i.isupper():
#         v = getattr(settings,i)
#         new_dict[i] = v
# print(new_dict)
# {'AGE': 18, 'INFO': '炎龙侠你完蛋了'}


# 模拟操作系统cmd终端执行用户命令
# class WinCmd(object):
#     def dir(self):
#         print('dir获取当前目录下所有的文件名称')
#
#     def ls(self):
#         print('ls获取当前路径下所有的文件名称')
#
#     def ipconfig(self):
#         print('ipconfig获取当前计算机的网卡信息')
#
# obj = WinCmd()
# while True:
#     cmd = input('请输入您的命令>>:').strip()
#     if hasattr(WinCmd(), cmd):
#         cmd = getattr(WinCmd(), cmd)
#         cmd()
#     else:
#         print(f'{cmd}不是内部或外部命令，也不是可运行的程序或批处理文件')
























