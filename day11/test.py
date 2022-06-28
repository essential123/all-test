command_dict = {
    '1': ['添加用户名功能'],
    '2': ['查看所有用户名功能'],
    '3': ['删除指定用户名功能'],
    '4': ['退出']
}

user_list = []

while True:
    for k, v in command_dict.items():
        print(k, v[0])
    command = input('请输入您要执行的功能的数字>>:').strip()
    if command == '1':
        user = input('请输入您要添加的用户>>:').strip()
        if user not in user_list:
            user_list.append(user)
            print(f'用户:{user}添加成功')
        else:
            print('用户已存在')
    elif command == '2':
        for username in user_list:
            print(
                f'''
                -------------------info------------------
                user:{username}
                -----------------------------------------
                '''
            )
    elif command == '3':
        target_user = input('请输入您要添加的用户>>:').strip()
        if target_user in user_list:
            user_list.remove(target_user)
            print(f'用户名{target_user}删除成功')
        else:
            print('删除的用户名不存在')
    elif command == '4':
        exit()
    else:
        print('输入有误，请重新输入')
