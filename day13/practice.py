# 1.编写简易版本的拷贝工具
#     自己输入想要拷贝的数据路径 自己输入拷贝到哪个地方的目标路径
#     任何类型数据皆可拷贝
#     ps:个别电脑C盘文件由于权限问题可能无法拷贝 换其他盘尝试即可
# with open(r'D:\百度云盘download\python基础day13\代码\day10\111.png','rb')as f1,open('lover.png','wb')as f2:
#     data = f1.read()
#     f2.write(data)


# 2.利用文件充当数据库编写用户登录、注册功能
#     文件名称:userinfo.txt
#     基础要求:
# 用户注册功能>>>:文件内添加用户数据(用户名、密码等)
# 用户登录功能>>>:读取文件内用户数据做校验
# ps:上述功能只需要实现一次就算过关(单用户) 文件内始终就一个用户信息
#      拔高要求:
#       用户可以连续注册
#            用户可以多账号切换登录(多用户) 文件内有多个用户信息
# ps:思考多用户数据情况下如何组织文件内数据结构较为简单
# 提示:本质其实就是昨天作业的第二道题 只不过数据库由数据类型变成文件

# print('''
#     1,注册
#     2,登录
# ''')
# user_info = {}
# with open('userinfo.txt','wt',encoding='utf-8')as f:
#     choice = input('请输入指令功能>>:').strip()
#     if choice == '1':
#         id = input('请输入您的id>>:').strip()
#         if id:
#             username = input('请输入您的用户名>>:').strip()
#             password = input('请输入您的密码>>:').strip()
#             f.write(f'id：{id},username:{username},password:{password}')
#         else:
#             print('输入不能为空')
#     elif choice == '2':
#         id = input('请输入您的id>>:').strip()
#         if id:
#             username = input('请输入您的用户名>>:').strip()
#             password = input('请输入您的密码>>:').strip()
#         else:
#             print('输入不能为空')
#     else:
#         print('输入有误，请输入正确的指令')


print('''
    1,注册
    2,登录
''')

while True:
    choice = input('请输入指令功能>>:').strip()
    if choice == '1':
        username = input('请输入您的用户名>>:').strip()
        password = input('请输入您的密码>>:').strip()
        if username and password:
            f1 = open('userinfo.txt', 'at', encoding='utf-8')
            data =f'username:{username},password:{password}'
            f1.write(data)
            f1.close()
        else:
            print('输入不能为空')
    elif choice == '2':
        with open('userinfo.txt', 'rt', encoding='utf-8') as f2:
            username = input('请输入您的用户名>>:').strip()
            password = input('请输入您的密码>>:').strip()
            if username and password:
                user,pwd = f2.read()
                if username == user and password == pwd:
                    print('登录成功')
                else:
                    print('账户或者密码错误')
            else:
                print('输入不能为空')
    else:
        print('输入有误，请输入正确的指令')




































































































