# 1.利用列表编写一个员工姓名管理系统
#     输入1执行添加用户名功能
#     输入2执行查看所有用户名功能
#     输入3执行删除指定用户名功能
#     ps:思考如何让程序循环起来并且可以根据不同指令执行不同操作
#     提示: 循环结构 + 分支结构
#     拔高: 是否可以换成字典或者数据的嵌套使用完成更加完善的员工管理而不是简简单单的一个用户名(能写就写 不会没有关系)
def add_user():
    user = input('请输入您要添加的用户>>:').strip()
    if user not in user_list:
        user_list.append(user)
        print('%s用户添加成功' % user)


def look_user():
    print(user_list)


def delete_user():
    user = input('请输入您要添加的用户>>:').strip()
    if user in user_list:
        user_list.remove(user)
        print('%s用户删除成功' % user)
    else:
        print('删除的用户名不存在')


def quit():
    exit()


command_list = {
    '1': ['添加用户名功能', add_user],
    '2': ['查看所有用户名功能', look_user],
    '3': ['删除指定用户名功能', delete_user],
    '4': ['退出', quit]
}

user_list = []

while True:
    for k, v in command_list.items():
        print(k, v[0])
    command = input('请输入您要执行的功能的数字>>:').strip()
    if command in command_list.keys():
        command_list[command][1]()
    else:
        print('输入有误，请重新输入')

# # 2.去重下列列表并保留数据值原来的顺序
# #     eg: [1,2,3,2,1] 去重之后 [1,2,3]
# l1 = [2,3,2,1,2,3,2,3,4,3,4,3,2,3,5,6,5]
# #
# # 方法一：
# l2=[]
# # # 循环l1得到l1列表的每一个值
# for i in l1:
#     if i not in l2:    # 如果列表l1的元素不在l2列表中，将这些值添加到l2
#         l2.append(i)
# print(l2)
# #
# # 方法二：
# l2=list(set(l1))
# l2.sort(key=l1.index)
# print(l2)

# 3.有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# pythons={'jason','oscar','kevin','ricky','gangdan','biubiu'}
# linuxs={'kermit','tony','gangdan'}

# 1. 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# {'gangdan'}

# 2. 求出所有报名的学生名字集合
# print(pythons | linuxs)
# {'kermit', 'gangdan', 'ricky', 'tony', 'kevin', 'biubiu', 'oscar', 'jason'}

# 3. 求出只报名python课程的学员名字
# print(pythons - linuxs)
# {'ricky', 'biubiu', 'kevin', 'jason', 'oscar'}

# 4. 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)
# {'oscar', 'biubiu', 'ricky', 'kevin', 'tony', 'kermit', 'jason'}
