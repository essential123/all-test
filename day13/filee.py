import os
import sys

file_name = "userinfo.txt"


def choiceTwo():
    username = input('input username>>:').strip()
    password = input('input password>>:').strip()

    if username and password:
        f = open(file_name, 'a', encoding='utf-8')
        data = f'{username}:{password}\n'

        f.write(data)
        f.close()

        print("sign in")
    else:
        print('error: sign in failed')


def choiceOne():
    fusers = []

    with open(file_name, 'r', encoding='utf-8') as f:
        username = input('please, input your name>>:').strip()
        password = input('please, input your password>>:').strip()

        login_user = username + ':' + password

        if username and password:
            pass
        else:
            print('error: please input again.')

        fli = f.readlines()
        if fli:
            pass
        else:
            print('error: xxxxxx')

        for i in fli:
            li = i.replace('\n', '')
            fusers.append(li)

    if login_user in fusers:
        print("logined")
    else:
        print('error: xxxxxx')



def inFunc():
    while True:

        print('''
            1,login
            2,sign in
            3.exit
        ''')

        choice = input('input number >>:').strip()

        if choice == '1':
            choiceOne()
        elif choice == '2':
            choiceTwo()
        elif choice == '3':
            sys.exit(0)
        else:
            print('>> Please, Input number again.')


if __name__ == '__main__':

    if os.path.exists(file_name):
        pass
    else:
        os.mknod(file_name)

    inFunc()
