'''
有下列用户数据
user_data = {
    '1': {'name': 'jason', 'pwd': '123', 'access': ['1', '2', '3']},
    '2': {'name': 'kevin', 'pwd': '321', 'access': ['1', '2']},
    '3': {'name': 'oscar', 'pwd': '222', 'access': ['1']}
}
并有三个函数
def func1():
    pass
def func2():
    pass
def func3():
    pass
要求:调用上述三个函数的时候需要从user_data中校验用户身份是否正确
并获取当前登录用户拥有的可执行函数功能编号即键access对应的功能编号列表 func1是1、func2是2、func3是3
并且一旦用户登录成功之后后续函数的调用不再校验用户身份请思考如何获取函数功能编号 如何校验用户身份 如何校验权限
ps:装饰器知识 附赠:实现上述主体功能即可 其他扩展优化功能可暂且不写
'''

user_data = {
    '1': {'name': 'jason', 'pwd': '123', 'access': ['1', '2', '3']},
    '2': {'name': 'kevin', 'pwd': '321', 'access': ['1', '2']},
    '3': {'name': 'oscar', 'pwd': '222', 'access': ['1']}
}


def outter(func_name):
    def wrapper(*args, **kwargs):
        if username == user_data[choice]['name'] and password == user_data[choice]['pwd']:
            access_list = user_data[choice]['access']
            if str(args[0]) in access_list:
                res = func_name(*args, **kwargs)
                return res
            else:
                print('当前用户暂无此编号:%s函数的权限' % args[0])
        else:
            print('用户名或者密码错误')

    return wrapper


@outter
def func1(*args, **kwargs):
    print('from func1')


@outter
def func2(*args, **kwargs):
    print('from func2')


@outter
def func3(*args, **kwargs):
    print('from func3')


if __name__ == '__main__':

    choice = input('请输入编号>>:').strip()
    if choice:
        username = input('请输入名字>>:').strip()
        password = input('请输入密码>>:').strip()

        func1(1, choice, username, password)
        func2(2, choice, username, password)
        func3(3, choice, username, password)
