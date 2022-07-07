# username = input('请输入用户名》》：')
# info = '欢迎' if username=='jason' else '滚蛋'
# print(info)

# name_list = ['jason','kevin','oscar','jerry']

# new_name_list = []
# for name in name_list:
#     new_name= name + '_NB'
#     new_name_list.append(new_name)
# print(new_name_list)

# new_name_list = [ name+'_NB' for name in name_list]
# print(new_name_list)

# dic = {
#     'jason':99,
#     'tony':100,
#     'tom':101,
# }
# res = max(dic)
#
# res1 = max(dic,key=lambda x:dic.get(x))
# print(res)
# print(res1)
#
# l1 = [1,2,3,4,5,6]
# res = map(lambda x:x+20,l1)
# print(list(res))

# def index(i):
#     return i+20
# res = map(index,l1)
# print(list(res))

# new_l1 = [int(i)+20 for i in l1]
# print(new_l1)

# new_l1 = filter(lambda x:x!=1,l1)
# print(list(new_l1))

# from functools import reduce
#
# res = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5],100)
# print(res)

# l1 = [11, 22, 33, 44, 55, 66]
#
# new_l1 = map(lambda x:x+20,l1)
# print(list(new_l1))

# n1 = [1, 2, 3,4]
# n2 = ['jason', 'kevin', 'oscar','tom']
# n3 = 'jack'
# res = zip(n1, n2, n3)
# print(res)  # <zip object at 0x000000000125E840>
# print(list(res))  # [(1, 'jason', 'j'), (2, 'kevin', 'a'), (3, 'oscar', 'c'), (4, 'tom', 'k')]

# l1 = ['jason', 'kevin', 'oscar', 'tony']
# print(list(filter(lambda x: x=='tonm',l1)))
# from functools import reduce
#
# l2 = [1,2,3]
# new_l2 = reduce(lambda x,y:x+y,l2)
# print(new_l2)


class Iter(object):
    def __init__(self):
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.counter+=1
        if self.counter==3:
            raise StopIteration()
        return self.counter













