import os
import json

base_path = os.path.dirname(__file__)
db_path = os.path.join(base_path, 'database')
if not os.path.exists(db_path):
    os.mkdir(db_path)
user_status = {
    'username': '',
    'is_login': False
}


def auth_user(func_name):
    def inner(*args, **kwargs):
        if user_status.get('is_login'):
            res = func_name(*args, **kwargs)
            return res
        else:
            print('用户未登录，请先登录')
            login()

    return inner


def register():
    while True:
        username = input('请输入用户名>>:').strip()
        file_list = os.listdir(db_path)
        if username in file_list:
            print('%s用户已存在' % username)
            continue
        if username:
            file_path = os.path.join(db_path, username)
            password = input('请输入密码>>:').strip()
            twice_password = input('请再次输入密码>>:').strip()
            if not password == twice_password:
                print('两次输入密码不一致')
                continue
            user_data = {
                'username': username,
                'password': password,
                'shopping_cards': {},
                'balance': 15000
            }
            with open(file_path, 'w', encoding='utf8') as f:
                json.dump(user_data, f)
                print('%s注册成功' % username)
                return


def login():
    while True:
        username = input('请输入用户名>>:').strip()
        if username:
            if username == user_status['username']:
                if user_status['is_login']:
                    print('%s用户已登录' % username)
                    continue
            file_path = os.path.join(db_path, username)
            if not os.path.isfile(file_path):
                print('用户名不存在,请先注册')
                break
            password = input('请输入密码>>:').strip()
            with open(file_path, 'r', encoding='utf8') as f:
                user_data = json.load(f)
            if username == user_data.get('username') and password == user_data.get('password'):
                user_status['is_login'] = True
                user_status['username'] = username
                print('%s登录成功' % username)
                return
            else:
                print('用户未注册，请先注册')
                break
        else:
            print('输入不能为空')


goods_list = [
    ['挂壁面', 3],
    ['印度飞饼', 22],
    ['极品木瓜', 666],
    ['土耳其土豆', 999],
    ['伊拉克拌面', 1000],
    ['董卓戏张飞公仔', 2000],
    ['仿真玩偶', 10000]
]


@auth_user
def add_shopping_cards():
    shop_car = {}
    while True:
        for i, j in enumerate(goods_list):
            print(f"商品编号:{i} , 商品名称：{j[0]} , 商品价格：{j[1]}")
        goods_choice = input('请输入你想要的商品编号(输入q退出)>>:').strip()
        if goods_choice == 'q':
            break
        elif int(goods_choice) in range(len(goods_list)):
            goods = goods_list[int(goods_choice)][0]
            goods_count = input('请输入你想要的商品数量>>:').strip()
            goods_price = goods_list[int(goods_choice)][1]
            shop_car[goods] = [goods_count, goods_price]
            file_path = os.path.join(db_path, '%s' % user_status['username'])
            with open(file_path, 'r', encoding='utf8') as f:
                user_data = json.load(f)
                old_shop_car = user_data.get('shopping_cards')
            for goods in shop_car:
                if goods in old_shop_car:
                    old_shop_car.get(goods)[0] += shop_car.get(goods)[0]
                else:
                    old_shop_car[goods] = shop_car.get(goods)
            with open(file_path, 'w', encoding='utf8') as f:
                json.dump(user_data, f)
            print('添加购物车成功')
            return

        else:
            print('请输入正确的编号')


@auth_user
def check_shop_car():
    file_path = os.path.join(db_path, user_status.get('username'))
    with open(file_path, 'r', encoding='utf8') as f:
        user_dict = json.load(f)
        shop_card_info = user_dict.get('shopping_cards')
        if not shop_card_info:
            print('购物车未添加任何物品')
        for item in shop_card_info.items():
            print(f"商品名称:{item[0]}  |  商品数量:{item[1][0]}  |  商品单价:{item[1][1]}")


@auth_user
def settlement_shopping_cards():
    file_path = os.path.join(db_path, user_status.get('username'))
    with open(file_path, 'r', encoding='utf8') as f:
        user_dict = json.load(f)
        shop_card_info = user_dict.get('shopping_cards')
        if not shop_card_info:
            print('购物车未添加任何物品')
        for item in shop_card_info.items():
            print(f"商品名称:{item[0]}  |  商品数量:{item[1][0]}  |  商品单价:{item[1][1]}")
        total_money = 0
        current_balance = user_dict.get('balance')
        for values in shop_card_info.values():
            values[0] = int(values[0])
            total_money += values[0] * values[1]
        if current_balance > total_money:
            current_balance -= total_money
            user_dict['balance'] = current_balance
            user_dict['shopping_cards']={}
            with open(file_path, 'w', encoding='utf8') as f:
                json.dump(user_dict, f)
            print(f'您今日消费：{total_money},您的余额为:{current_balance}')
        else:
            print('余额不足，请充值')
            return


def out():
    exit()


command_dict = {
    '1': ['用户注册', register],
    '2': ['用户登录', login],
    '3': ['添加购物车', add_shopping_cards],
    '4': ['查看购物车', check_shop_car],
    '5': ['结算购物车', settlement_shopping_cards],
    'q': ['退出', out]
}


def run():
    while True:
        for k, v in command_dict.items():
            print(k, v[0])
        choice = input('请输入功能编号>>:').strip()
        if choice in command_dict:
            command_dict[choice][1]()
        else:
            print('编号超出范围，请重新输入')


if __name__ == '__main__':
    run()
