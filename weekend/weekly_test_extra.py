# 附加题
user_data = {
    '1': {'name': 'jason', 'pwd': '123', 'access': ['1', '2', '3']},
    '2': {'name': 'kevin', 'pwd': '321', 'access': ['1', '2']},
    '3': {'name': 'oscar', 'pwd': '222', 'access': ['1']}
}
def outter(func_name):
    def info(*args, **kwargs):
        choice = input('请输入编号>>:').strip()
        if choice:
            username = input('请输入编号>>:').strip()
            password = input('请输入编号>>:').strip()
            if username == user_data[choice]['name'] and password == user_data[choice]['pwd']:
                print('登录成功')
                access_list = user_data[choice]['access']
                res = func_name(*args, **kwargs)
                return res
            else:
                print('用户名或者密码错误')
        else:
            print('编号不能为空')
    return info

@outter
def func1():
    print('from func1')
@outter
def func2():
    print('from func2')

@outter
def func3():
    print('from func3')