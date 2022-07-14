# import os
# source = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(source)

# from collections import namedtuple
# Point = namedtuple('二维坐标系',['x','y'])
# res =Point(1,2)
# print(res)

# l1 =[1,2,3,4]
# l1.pop(1)
# print(l1)

from collections import namedtuple
# p=namedtuple('扑克牌',['花色','点数'])
# res = p('♦','5')
# print(res)

# from collections import deque
# l1 = [1,2,3,4]
# q =deque(l1)
# q.append(999)
# print(q)

from collections import OrderedDict
# d = dict([('a',1),('b',2)])
# print(d)

# from collections import Counter
# res = 'qwertyuiosdfghjkwertyhvn'
# print(Counter(res))

from collections import defaultdict
staff_dict=defaultdict()
# staff_dict = defaultdict(int)
staff_dict['name']='jaosn'
print(staff_dict['name'])
print(staff_dict['age'])

# import time
# time.struct_time
# time.