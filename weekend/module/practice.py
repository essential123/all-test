import json
import os


# 4.周末大作业(尝试编写)
# 	# 项目功能
#   		1.用户注册
#     	2.用户登录
#     	3.添加购物车
#     	4.结算购物车
# 	# 项目说明
#   		用户数据采用json格式存储到文件目录db下 一个用户一个单独的文件
#     	数据格式 {"name":"jason","pwd":123}
#        		# ps:文件名可以直接用用户名便于校验
#     	用户注册时给每个用户添加两个默认的键值对(账户余额 购物车)
#     		{"balance":15000,"shop_car":{}}
#     	添加购物车功能 商品列表可以自定义或者采用下列格式
#             good_list = [
#                     ['挂壁面',3]
#                     ['印度飞饼', 22]
#                 	['极品木瓜', 666],
#                 	['土耳其土豆', 999],
#                 	['伊拉克拌面', 1000],
#                 	['董卓戏张飞公仔', 2000],
#                 	['仿真玩偶', 10000]
#             ]
#       用户可以反复添加商品，在购物车中记录数量
#       		{'极品木瓜':[个数,单价]}
#     	结算购物车
#     		获取用户购物车中所有的商品计算总价并结算即可
# 	 针对添加购物车和结算只有登录的用户才可以执行


def outter(func):
    def wrapper(*args, **kwargs):
        if status_data['is_login']:
            res = func(*args, **kwargs)
            return res
        else:
            login()

    return wrapper


good_list = [
    ['挂壁面', 3],
    ['印度飞饼', 22],
    ['极品木瓜', 666],
    ['土耳其土豆', 999],
    ['伊拉克拌面', 1000],
    ['董卓戏张飞公仔', 2000],
    ['仿真玩偶', 10000],
]

file_name = 'userinfo.txt'

status_data = {
    'username': None,
    'is_login': False
}


def register():
    info = []
    if status_data['is_login']:
        print('%s已登录' % status_data['username'])
        return
    while True:
        username = input('请输入您的用户名>>:').strip()
        with open(file_name, 'r') as f:
            for line in f:
                print(line, type(line))
                # real_name = line['username']
                real_name = json.load(f)
                print(real_name, type(real_name))
                if username == real_name:
                    print('用户名已存在')
                    break
            else:
                password = input('请输入您的密码>>:').strip()
                if password:
                    # user_info = '%s,%s\n' % (username, password)
                    user_info = {'username': username, 'password': password, 'balance': 100000,'shopping_cart':[]}
                    with open(file_name, 'a') as f:
                        # json.dump(user_info, f,end='\n')
                        info_dic = json.dump(user_info, f)
                        info.append(info_dic)
                        # f.write(user_info)
                    print(f'{username}注册成功')
                    break
                else:
                    print('输入不能为空')


def login():
    while True:
        if status_data['is_login']:
            print('%s已登录' % status_data['username'])
            return
        username = input('请输入您的用户名>>:').strip()
        password = input('请输入您的密码>>:').strip()
        with open(file_name, 'r') as f:
            data = json.load(f)
            user, pwd = data['username'], data['password']
            if user == username and pwd == password:
                status_data['is_login'] = True
                status_data['username'] = username
                print('%s成功登录' % status_data['username'])
                break
            else:
                print('用户名或者密码错误')


@outter
def add_shopping_cart():
    for i in good_list:
        print(i)
    choice = input('请输入你想要购买的商品>>:').strip()
    if choice in good_list[0]:
        with open(file_name, 'r') as f:
            data = json.load(f)
        with open(file_name, 'a') as f:
            data['shopping_cart'].append(choice)
            print(data)
            json.dump(data,f)


@outter
def Settlement_shopping_cart():
    pass


def out():
    exit()


command_dict = {
    '1': ['用户注册', register],
    '2': ['用户登录', login],
    '3': ['添加购物车', add_shopping_cart],
    '4': ['结算购物车', Settlement_shopping_cart],
    'q': ['退出', out]
}


def main_body():
    while True:
        for i, command in command_dict.items():
            print(i, command_dict[i][0])
        choice = input('请输入您的指令>>:').strip()
        if choice in command_dict:
            command_dict[choice][1]()
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':

    if os.path.exists('userinfo.txt'):
        pass
    else:
        with open('userinfo.txt', 'a', encoding='utf-8') as f:
            pass

    main_body()
