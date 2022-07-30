# person1 = {
#     'name': 'jason',
#     'p_type': '猛男',
#     'attack_val': 800,
#     'life_val': 2000
# }
# dog1 = {
#     'name': '小黑狗',
#     'd_type': '泰迪',
#     'attack_val': 50,
#     'life_val': 800
# }
#
# def get_person(name, gender, age, p_type, attack_val, life_val):
#     person_obj = {
#         'name': name,
#         'gender': gender,
#         'age': age,
#         'p_type': p_type,
#         'attack_val': attack_val,
#         'life_val': life_val
#     }
#     return person_obj
#
# def get_dog(name, d_type, attack_val, life_val):
#     dog_obj = {
#         'name': name,
#         'd_type': d_type,
#         'attack_val': attack_val,
#         'life_val': life_val
#     }
#     return dog_obj
#
# def person_attack(person_obj, dog_obj):
#     print('即将被攻击的狗:%s 当前血量:%s' % (dog_obj.get('name'), dog_obj.get('life_val')))  # 先展示当前狗的状态
#     dog_obj['life_val'] -= person_obj.get('attack_val')  # 人锤狗 直接用狗的生命值减去人的攻击力
#     print('人:%s 锤了 狗:%s 狗掉血:%s 剩余血量:%s' % (person_obj.get('name'), dog_obj.get('name'), person_obj.get('attack_val'), dog_obj.get('life_val')))
#
#
# def dog_attack(dog_obj, person_obj):
#     print('即将被攻击的人:%s 当前血量:%s' % (person_obj.get('name'), person_obj.get('life_val')))  # 先展示当前人的状态
#     person_obj['life_val'] -= dog_obj.get('attack_val')  # 狗咬人 直接用人的生命值减去狗的攻击力
#     print('狗:%s 咬了 人:%s 人掉血:%s 剩余血量:%s' % (dog_obj.get('name'), person_obj.get('name'), dog_obj.get('attack_val'), person_obj.get('life_val')))
#
# p1 = get_person('jason', 'male', 18, '猛男', 800, 1000)
# d1 = get_dog('小黑', '松狮犬', 300, 500)
# # 狗咬人
# dog_attack(d1,p1)
# print(p1)
# # 人揍狗
# person_attack(p1, d1)
# print(dog1)

#
# person1 = {
#     'name': 'jason',
#     'p_type': '猛男',
#     'attack_val': 800,
#     'life_val': 2000
# }
#
#
# dog1 = {
#     'name': '小黑狗',
#     'd_type': '泰迪',
#     'attack_val': 50,
#     'life_val': 800
# }


# def person_info(name, p_type, attack_val, life_val):
#     person1_dict = {
#         'name': name,
#         'p_type': p_type,
#         'attack_val': attack_val,
#         'life_val': life_val
#     }
#     return person1_dict
#
#
# def dog_info(name, p_type, attack_val, life_val):
#     dog_dict = {
#         'name': name,
#         'p_type': p_type,
#         'attack_val': attack_val,
#         'life_val': life_val
#     }
#     return dog_dict
#
#
# def person_attack(person_info, dog_info):
#     print('即将被攻击的狗是%s 当前血量：%s' % (dog_info.get('name'), dog_info.get('life_val')))
#     dog_info['life_val'] -= person_info['attack_val']
#     print('人:%s,锤了狗%s，狗掉血:%s,剩余血量%s' % (
#         person_info.get('name'), dog_info.get('name'), person_info.get('attack_val'), dog_info.get('life_val')))
#
#
# def dog_attack(dog_info, person_info):
#     print('即将被攻击的人:%s 当前血量:%s' % (person_info.get('name'), person_info.get('life_val')))  # 先展示当前人的状态
#     person_info['life_val'] -= dog_info.get('attack_val')  # 狗咬人 直接用人的生命值减去狗的攻击力
#     print('狗:%s 咬了 人:%s 人掉血:%s 剩余血量:%s' % (
#         dog_info.get('name'), person_info.get('name'), person_info.get('attack_val'), person_info.get('life_val')))
#
#
# d1 = dog_info('jason', '猛男', 8000, 9000)
# p1 = person_info('小黑狗', '巴哥犬', 200, 500)
# dog_attack(d1, p1)


class Student:
    school = '清华大学'

    def __init__(self, name):
        self.name = name

    def choice_course(self):
        print('正在选课')


# print(Student.__dict__)
# print(Student.__dict__['school'])
# print(Student.__dict__.get('school'))
# obj1 = Student()
# obj1.__dict__['name'] = 'jason'
# print(obj1.name)


# obj1 = Student('jason')
# print(obj1.name)
# print(obj1.__dict__.get('name'))
# print(obj1.__dict__['name'])