# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# res = l1.__iter__()
# while True:
#     try:
#         print(res.__next__())
#     except Exception as e:
#         break
#
#
# def index():
#     return 123, 123, 123
#
#
# res = index()
# print(res)
#
#
# def func():
#     print('123')
#     yield 123, 123, 123
#
#
# res = func()
# print(res.__next__())
#
# for i in range(10):
#     print(i)
#
#
# def index():
#     print('1~')
#     yield 111, 222, 333
#     print('2~')
#     yield 222
#     print('3~')
#     yield 333
#
#
# print(index)  # <function index at 0x000001F499F7A5E0>
# res = index()
# print(res)  # <generator object index at 0x0000021E18BACA50>
# res.__next__()  # 1~
# res.__next__()  # 2~
# res.__next__()  # 3~
# res.__next__()  # StopIteration
#
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())


def add(n, i):  # 普通函数 返回两个数的和  求和函数
    return n + i


def test():  # 生成器
    for i in range(4):
        yield i  # (0,1,2,3)


g = test()  # 激活生成器[函数体有yield的，函数名加括号调用，产生返回值（用g接收一下返回值）,g变成了一个迭代器对象(生成器)]

for n in [1, 10]:  # n第一次循环是1，第二次循环是10
    g = (add(n, i) for i in g)
    """
    第一次for循环
        g = (add(1, i) for i in g)
    第二次for循环
        g = (add(10, i) for i in (add(10, i) for i in g))
    """
res = list(g)
print(res)
