import os

file_name = 'userinfo.txt'


def register():
    username = input('请输入您的用户名>>:').strip()
    with open(file_name, 'r') as f:
        for line in f:
            real_name=line.split(',')[0]
            if username == real_name:
                print('用户名已存在')
                break
        else:
            password = input('请输入您的密码>>:').strip()
            user_info = '%s,%s\n' %(username,password)
            with open(file_name, 'a') as f:
                f.write(user_info)
            print(f'{username}注册成功')
def login():
    username = input('请输入您的用户名>>:').strip()
    password = input('请输入您的密码>>:').strip()
    with open(file_name, 'r') as f:
        for line in f:
            real_name,real_pwd=line.split(',')
            if username==real_name and password==real_pwd.rstrip('\n'):
                print('登录成功')
                break
        else:
            print('用户名或者密码错误')


def out():
    exit()


command_dict = {
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['退出', out]
}


def main_body():
    while True:
        for choice, command in command_dict.items():
            print(choice, command_dict[choice][0])
        choice = input('请输入您的指令>>:').strip()
        if choice in command_dict:
            command_dict[choice][1]()
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':

    if os.path.exists(file_name):
        pass
    else:
        # with open(file_name, 'a', encoding='utf-8') as f:
        #     pass
        os.mknod(file_name)

    main_body()
