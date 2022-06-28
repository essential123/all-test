def add_staff():
    id = input('请输入员工的编号>>:').strip()
    if not id:
        print('员工编号不能为空')
    elif id not in staff_dict:
        name = input('请输入员工的姓名>>:').strip()
        age = input('请输入员工的年龄>>:').strip()
        job = input('请输入员工的岗位>>:').strip()
        salary = input('请输入员工的薪资>>:').strip()
        if not (name or age or job or salary):
            print('员工信息不能为空，请重新输入')
        else:
            staff_dict[id] = [name, age, job, salary]
            print(f'id为{id}的员工信息已添加')
    else:
        print('员工信息已存在')
def fix_staff():
    id = input('请输入员工的编号>>:').strip()
    if id in staff_dict:
        salary = input('请输入员工的薪资>>:').strip()
        staff_dict[id][3] = salary
        print(f'id为{id}的员工薪资修改成功')
    else:
        print('用户信息不存在')
def check_one_info():
    id = input('请输入员工的编号>>:').strip()
    print(staff_dict[id])
def check_all_info():
    print(staff_dict)
def delete_staff():
    id = input('请输入员工的编号>>:').strip()
    if id not in staff_dict:
        staff_dict.pop(id)
        print(f'id为{id}的员工数据已删除')
    else:
        print('用户信息不存在')
def quit():
    exit()
command_dict = {
    '1': ['添加员工信息',add_staff],
    '2': ['修改员工薪资',fix_staff],
    '3': ['查看指定员工',check_one_info],
    '4': ['查看所有员工',check_all_info],
    '5': ['删除员工数据',delete_staff],
    '6': ['退出',quit]
}
staff_dict = {}
while True:
    for k,v in command_dict.items():
        print(k,v[0])
    choice = input('请输入您的指令对应的数字>>:').strip()
    if choice in command_dict:
        command_dict[choice][1]()
    else:
        print('输入有误，请重新输入指令')