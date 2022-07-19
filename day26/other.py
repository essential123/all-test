import json
import os

# 1.先获取执行文件所在的路径
base_dir = os.path.dirname(__file__)
# 2.拼接db文件夹的路径
db_dir = os.path.join(base_dir, 'db')
# 3.判断db路径是否已存在 如果存在则无需创建 不存在则自动创建
if not os.path.exists(db_dir):
    os.mkdir(db_dir)

is_login = {
    'username': '',  # 用户登录成功之后 记录用户名 便于后续查找并修改用户对应的数据
}


# 校验用户登录装饰器
def login_auth(func_name):
    def inner(*args, **kwargs):
        # 1.判断全局字典键username是否已经有值
        if is_login.get('username'):
            res = func_name(*args, **kwargs)
            return res
        else:
            print('请先登录')
            # login()  # 自动调用登录函数完成登录操作

    return inner


@login_auth
def add_shop_car():
    # 1.获取商品数据(直接编写)
    good_list = [
        ['挂壁面', 3],
        ['印度飞饼', 22],
        ['极品木瓜', 666],
        ['土耳其土豆', 999],
        ['伊拉克拌面', 1000],
        ['董卓戏张飞公仔', 2000],
        ['仿真玩偶', 10000]
    ]
    # 定义一个临时存储用户想要购买商品的字典数据  {'印度飞饼':[10, 22], '仿真玩偶':[1, 10000]}
    temp_shop_dict = {}
    # 2.循环打印商品信息购用户选择
    while True:
        for i, j in enumerate(good_list):  # i 数值    j 列表
            print(f"商品编号:{i}    |   商品名称:{j[0]}     |   商品单价:{j[1]}")
        target_good_id = input('请输入想要购买的商品编号(q)>>>:').strip()
        if target_good_id == 'q':
            file_path = os.path.join(db_dir, '%s.json' % is_login.get('username'))
            with open(file_path, 'r', encoding='utf8') as f:
                user_dict = json.load(f)
            old_shop_car = user_dict.get('shop_car')
            for good_name in temp_shop_dict:
                if good_name in old_shop_car:
                    old_shop_car.get(good_name)[0] += temp_shop_dict.get(good_name)[0]
                else:
                    old_shop_car[good_name] = temp_shop_dict.get(good_name)
            user_dict['shop_car'] = old_shop_car
            with open(file_path, 'w', encoding='utf8') as f:
                json.dump(user_dict, f)
            print('添加购物车成功')
            return
        if not target_good_id.isdigit():
            print('商品编号只能是数字')
            continue
        target_good_id = int(target_good_id)
        if target_good_id not in range(len(good_list)):
            print('商品编号超出了范围')
            continue
        target_good_info = good_list[target_good_id]  # ['印度飞饼', 22]
        target_good_name = target_good_info[0]
        target_good_price = target_good_info[1]
        target_good_num = input('请输入想要购买的商品数量>>>:').strip()
        if not target_good_num.isdigit():
            print('商品数量只能是数字')
            continue
        target_good_num = int(target_good_num)
        if target_good_name in temp_shop_dict:
            value_list = temp_shop_dict.get(target_good_name)  # [5, 22]
            value_list[0] += target_good_num  # [5+5, 22]
            temp_shop_dict[target_good_name] = value_list
        else:
            temp_shop_dict[target_good_name] = [target_good_num, target_good_price]


@login_auth
def buy_shop_car():
    # 1.拼接用户文件完整路径
    file_path = os.path.join(db_dir, '%s.json' % (is_login.get('username'),))
    # 2.读取用户数据
    with open(file_path, 'r', encoding='utf8') as f:
        user_dict = json.load(f)
    '''
    print(user_dict)  # {'name': 'jason', 'pwd': '123', 'balance': 15000, 
    'shop_car': {'挂壁面': [100, 3], '土耳其土豆': [50, 999], '印度飞饼': [33, 22]}}
    '''
    # 3.获取购物车商品数据
    shop_car = user_dict.get('shop_car')  # {'挂壁面': [100, 3], '土耳其土豆': [50, 999], '印度飞饼': [33, 22]}
    if not shop_car:
        print('你先去买东西 行不行')
        return
    # 4.计算商品的总价
    total_money = 0
    current_balance = user_dict.get('balance')
    for values in shop_car.values():  # [100, 3]
        total_money += values[0] * values[1]
    # 5.判断余额是否充足
    if current_balance >= total_money:
        rest_money = current_balance - total_money
        user_dict['balance'] = rest_money
        user_dict['shop_car'] = {}
        with open(file_path, 'w', encoding='utf8') as f:
            json.dump(user_dict, f)
        print(f'今日消费:{total_money} 卡上余额:{rest_money}')
    else:
        print('你个穷逼 钱不够')
        return
