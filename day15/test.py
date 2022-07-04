# l1 = [1,2,3,4,7,55,6]
# def my_len():
#     count = 0
#     for i in l1:
#         count+=1
#     return count
# res = my_len()
# print(res)

# def func():
#     print('xxx')
# func
# def func():
#     print('xxx')
# name='xxxxxxxxxxxxx'
# name = func
# print(name)
# def func():
#     print('xxx')
# name = 'jason'
# func = name


# info1 = '尊敬{}客户你好！你{}月共消费{}元，剩余话费是{}'.format('tom', 5, 100, 99)
# print(info1)
# info3 = 'my name is {name}, my age is {age}!'.format(age=18,name='tony')
# print(info3)
#
# info4 = 'my name is {0}, my age is {1}!'.format('tony', 18)
# print(info4)
#
# name = 'kevin'
# age = 18
# print(f'my name is {name} my age is {age} ')


# l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# a, b, *c, d = l1  # *在解压赋值的时候会自动将多余的数据值组织成列表赋值给*号后面的变量名
# print(a)  # 11
# print(b)  # 22
# print(c)  # [33, 44, 55, 66, 77, 88]
# print(d)  # 99
#

# a = 10
# b = 10
# c = 5 + 5
# print(id(a),id(b),id(c))  # 140721252784064 140721252784064 140721252784064
# print(a is b is c)  # True


# while True:
#     username = input('username>>>:')
#     password = input('password>>>:')
#     if username == 'jason' and password == '123':
#         print('登录成功 欢迎光临 21号为您服务!!!')
#         while True:
#             cmd = input('请输入您的指令>>>:')
#             if cmd == 'q':
#                 print('欢迎下次光临')
#                 break
#             print('正在执行您的命令:%s'%cmd)
#         break
#     else:
#         print('用户名或密码错误')

# def factorial(number):
#     result = 1
#     while number>0:
#         result *= number
#         number -=1
#     return result
#
# number = input('请输入您需要计算的阶乘>>:').strip()
# new_num=int(number)
# print(factorial(new_num))

# import math
#
# def circle_area(r):
#     result = math.pi*r**2
#     return round(result,2)
#
# num = input('请输入圆的半径>>:').strip()
# r= ''.join(num)
# r = int(r)
# print(circle_area(r))

# even_list = []
#
#
# def even_number(begin, end):
#     for i in range(begin, end):
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
#
# number1 = input('请输入开始值>>:').strip()
# number2 = input('请输入结束值>>:').strip()
#
# begin =''.join(number1)
# end =''.join(number2)
# if begin and end:
#     print(even_number(int(begin), int(end)))
# else:
#     print('输入不能为空')
#
# number1 = input('请输入开始值>>:').strip()
# number2 = input('请输入结束值>>:').strip()
#
# begin =''.join(number1)
# end =''.join(number2)
# if begin and end:
#     even_numbers = [i for i in range(int(begin), int(end)) if i % 2 == 0]
#     print(even_numbers)
# else:
#     print('输入不能为空')

# a_list = [0 , 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64, 81]
# b_list = [x for x in a_list if x % 2 == 0]
# print(b_list)  # [0, 4, 16, 36, 64]


# def remove_multi_element(list1, list2):
#     for i in list2:
#         if i in list1:
#             list1.remove(i)
#
#     return list1
#
# raw_list = input('请输入原始列表数据>>:').strip()
#
# remove_element = input('请输入要移除的元素>>:').strip()
# list1=raw_list.split(',')
# list2=remove_element.split(',')
# print(list1,type(list1))
# print(list2,type(list2))
# print(remove_multi_element(list1,list2))


# def remove_multi_element(raw_list, remove_element):
#     for i in remove_element:
#         raw_list.remove(i)
#     return raw_list
# raw_list = input('请输入原始列表数据>>:').strip().split(',')
#
# remove_element = input('请输入要移除的元素>>:').strip().split(',')
# print(remove_multi_element(raw_list,remove_element))


# raw_list = input('请输入原始列表数据>>:').strip().split(',')
# remove_element = input('请输入要移除的元素>>:').strip().split(',')
# data=[element for element in raw_list if element not in remove_element]
# print(data)

# list1 = [2,10,9,8,77,65,32]
# list2 = sorted(list1)
# print(list1,list2)

# tuple1 = (1, 2, 3, 4, 4, 8, 5, 1)
#
# tuple2 = sorted(tuple1)
#
# print(tuple2)

# stu_list = [
#     {'sno': 101, 'sname': '小张', 'sgrade': 88},
#     {'sno': 102, 'sname': '小王', 'sgrade': 77},
#     {'sno': 103, 'sname': '小李', 'sgrade': 99},
#     {'sno': 104, 'sname': '小赵', 'sgrade': 66}
# ]
#
# new_stu_list = sorted(stu_list,key=lambda x:x['sgrade'])
# print(new_stu_list)

# s_id = input('请输入您的学号>>:').strip()
# s_name = input('请输入您的姓名>>:').strip()
# s_score = input('请输入您的成绩>>:').strip()
# s_info = s_id + ',' + s_name + ',' + s_score + '\n'
#
# with open('student_info.txt','a',encoding='utf-8') as f1:
#     f1.write(s_info)
# with open('student_info.txt', 'r', encoding='utf-8') as f2:
#     sort_list = []
#     for line in f2:
#         new_line=line.rstrip('\n').split(',')
#         sort_list.append(new_line)
#     sort_stu_info = sorted(sort_list,key=lambda x:int(x[2]))
#     print(sort_stu_info)
#
# l3 = {111,123}
# l4 = {111,124}
# print(l4>l3)

# s_id = input('请输入您的学号>>:').strip()
# s_name = input('请输入您的姓名>>:').strip()
# s_score = input('请输入您的成绩>>:').strip()
# s_info = s_id + ',' + s_name + ',' + s_score + '\n'
# with open('student_info.txt', 'a', encoding='utf-8') as f1:
#     f1.write(s_info)
# with open('student_info.txt', 'r', encoding='utf-8') as f2:
#     sort_list = []
#     for line in f2:
#         new_line=line.rstrip('\n').split(',')
#         sort_list.append(new_line)
#     score = [int(i[2]) for i in sort_list]
#     print(max(score),min(score),round(sum(score)/len(score)))

# with open('artical.txt','r',encoding='utf-8') as f:
#     word_dict = {}
#     for line in f:
#         # word = line[:-1].split()
#         words = line.rstrip('\n').split()
#         print(words)
#         for word in words:
#             if word not in word_dict:
#                 word_dict[word]=0
#             word_dict[word]+=1
# print(word_dict)


# my_dict = {
#     'name':'jzb',
#     'age':18,
#     'sex':'man',
#     'hobby':'game'
# }
#
# my_dict.setdefault('name', 'xxx')
# my_dict.setdefault('job', 'python')
# print(my_dict)














