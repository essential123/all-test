# l1 = [1,2,3,4,5,6]
#
# print(l1.__iter__().__next__())
# print(l1.__iter__().__next__())
# print(l1.__iter__().__next__())

# print(dir(list))
# enumerate


# print(round(98.3))
# print(round(98.6))

# print(round(-0.6))
# print(round(1.5))
# print(round(2.5))
# print(round(-2.5))
# print(round(5.675,2))

# list1 = [1,2,3,4,5,6].__iter__()

# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# list1 = [1,2,3,4,5,6]
# print(list1.__iter__().__next__())
# print(list1.__iter__().__next__())
# print(list1.__iter__().__next__())

# list1=[1,2,3,4,5,6]
# res = list1.__iter__()
# print(res)  # <list_iterator object at 0x00000000012E9730>

# str1 = 'jason'
# res = str1.__iter__()
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

# l1 = [11, 22, 33, 44, 55, 66, 77, 88]
# res = l1.__iter__()
# count = 0
# while count<len(l1):
#     print(res.__next__())
#     count+=1

# print(abs(-1))
# print(all([1,2,3,44,5]))
# print(all([0,2,3,44,5]))
# print(any([0,2,3,44,5]))

# print(bin(10))
# print(oct(10))
# print(hex(10))

# print(chr(65))


# print(bytes('xxx','utf-8'))
# print(str(b'xxx','utf-8'))

# res = '人身苦短'
# print(bytes(res,'utf-8'))

# res = bytes('人身苦短','utf-8')
# print(str(res,'utf-8'))

# user_data = {
#     '1': {'name': 'jason', 'pwd': '123', 'access': ['1', '2', '3']},
#     '2': {'name': 'kevin', 'pwd': '321', 'access': ['1', '2']},
#     '3': {'name': 'oscar', 'pwd': '222', 'access': ['1']}
# }
#
# is_login = {
#     'is_login':False,
#     'access_list':[]
# }
#
# def auth_user(id):
#     def deco(func_name):
#         def inner(*args,**kwargs):
#             if is_login.get('is_login'):
#                 access =is_login.get('access_list')
#                 if id in access:
#                     res = func_name(*args,**kwargs)
#                     return res
#             else:
#                 user_id = input('请输入编号>>:').strip()
#                 if user_id in user_data:
#                     username = input('请输入姓名>>:').strip()
#                     password = input('请输入密码>>:').strip()
#                     real_dic = user_data.get(user_id)
#                     if username == real_dic.get('name') and password == real_dic.get('pwd'):
#                         access = real_dic.get('access')
#                         is_login['is_login'] = True
#                         is_login['access_list'] = access
#                         if id in access:
#                             res=func_name(*args,**kwargs)
#                             return res
#                     else:
#                         print('你没有当前功能编号为:%s 的函数执行权限' % id)
#         return inner
#     return deco
#
# @auth_user('1')  # 被装饰的函数 提前传入该函数的功能编号
# def func1():
#     print('from func1')
#
#
# @auth_user('2')  # 被装饰的函数 提前传入该函数的功能编号
# def func2():
#     print('from func2')
#
#
# @auth_user('3')  # 被装饰的函数 提前传入该函数的功能编号
# def func3():
#     print('from func3')
#
#
# func1()
# func2()
# func3()


user_data = {
    '1': {'name': 'jason', 'pwd': '123', 'access': ['1', '2', '3']},
    '2': {'name': 'kevin', 'pwd': '321', 'access': ['1', '2']},
    '3': {'name': 'oscar', 'pwd': '222', 'access': ['1']}
}

is_login = {
    'is_login': False,
    'access': []
}


def auth_user(func_id):
    def deco(func_name):
        def inner(*args, **kwargs):
            if is_login.get('is_login'):
                access = is_login.get('access')
                if func_id in access:
                    res = func_name(*args, **kwargs)
                    return res
                else:
                    print('你没有当前功能编号为:%s 的函数执行权限' % func_id)
            else:
                user_id = input('请输入编号>>:').strip()
                if user_id in user_data:
                    username = input('请输入名字>>:').strip()
                    password = input('请输入密码>>:').strip()
                    real_dic = user_data.get(user_id)
                    if username == real_dic.get('name') and password == real_dic.get('pwd'):
                        access = real_dic['access']
                        is_login['is_login'] = True
                        is_login['access'] = access
                        if func_id in access:
                            res = func_name(*args, **kwargs)
                            return res
                        else:
                            print('你没有当前功能编号为:%s 的函数执行权限' % func_id)
                else:
                    print('输入错误')

        return inner

    return deco


@auth_user('1')
def func1():
    print('from func1')


@auth_user('2')
def func2():
    print('from func2')


@auth_user('3')
def func3():
    print('from func3')


func1()
func2()
func3()
