# 1.统计列表中每个数据值出现的次数并组织成字典战士
# 	eg: l1 = ['jason','jason','kevin','oscar']
#       结果:{'jason':2,'kevin':1,'oscar':1}
# 	真实数据
#     	l1 = ['jason','jason','kevin','oscar','kevin','tony','kevin']

#
# l1 = ['jason','jason','kevin','oscar','kevin','tony','kevin']
# result_dict = {}
#
# for i in l1:
#     count = 0
#     if i not in result_dict:
#         count+=1
#         result_dict[i]=count
#     else:
#         result_dict[i]+=1
# print(result_dict)



# 2.编写员工管理系统
#     1.添加员工信息
#     2.修改员工薪资
#     3.查看指定员工
#     4.查看所有员工
#     5.删除员工数据
# 	 提示:用户数据有编号、姓名、年龄、岗位、薪资
#     数据格式采用字典:思考如何精准定位具体数据>>>:用户编号的作用

print('''
    1,添加员工信息
    2,修改员工薪资
    3,查看指定员工
    4,查看所有员工
    5,删除员工数据
    ''')
staff_dict = {}
while True:
    choice = input('请输入您的指令对应的数字>>:').strip()
    if choice == '1':
        id = input('请输入员工的编号>>:').strip()
        if not id:
            print('员工编号不能为空')
        elif id not in staff_dict :
            name = input('请输入员工的姓名>>:').strip()
            age = input('请输入员工的年龄>>:').strip()
            job = input('请输入员工的岗位>>:').strip()
            salary = input('请输入员工的薪资>>:').strip()
            if not name or age or job or salary:
                print('员工信息不能为空，请重新输入')
                continue
            else:
                staff_dict[id] = [name,age,job,salary]
                print(f'id为{id}的员工信息已添加')
        else:
            print('员工信息已存在')
    elif choice == '2':
        id = input('请输入员工的编号>>:').strip()
        if id in staff_dict:
            salary = input('请输入员工的薪资>>:').strip()
            staff_dict[id][3]=salary
            print(f'id为{id}的员工薪资修改成功')
        else:
            print('用户信息不存在')
    elif choice == '3':
        id = input('请输入员工的编号>>:').strip()
        print(staff_dict[id])
    elif choice == '4':
        print(staff_dict)
    elif choice == '5':
        id = input('请输入员工的编号>>:').strip()
        if not id:
            print('员工编号不能为空')
        elif id in staff_dict:
            staff_dict.pop(id)
            print(f'id为{id}的员工数据已删除')
        else:
            print('用户信息不存在')
    elif choice == 'q':
        print('退出')
        break
    else:
        print('输入有误，请重新输入指令')

































































































































































































