# 1.你所使⽤过的⽂本编辑器有哪些
'''

notepad++,Typora,文本文档(记事本)
# 其中Typora有何特点并简单列举⼏个语法功能
```+python回车  代码框
ctrl+数字   对应标题级别（1-6）
使用加号 + 子标题
'''

# 2.什么是编程语⾔，编程的本质是什么

'''
人与计算机之间沟通交流的媒介
用计算机能够读懂的语言写下来的一堆文件
'''

# 3.计算机五⼤组成部分及各⾃主要功能

'''
运算器：数字计算，逻辑运算
控制器  控制计算机各个硬件的工作
存储器：存储
    内存 
    外存（硬盘）
输入设备 向计算机传递信息
输出设备 向外部传递信息

运算器+控制器=cpu
'''

# 4.计算机三⼤核⼼硬件及详述三者⼯作关系

'''
cpu
内存
外存（硬盘）

每次执行程序的时候，都是先将硬盘资源加载到内存，然后cpu再去调用内存资源
'''

# 5.简述计算机底层存储数据原理及编程语⾔发展史、分类

'''
底层存储是一堆 1 0 1 0 1 0的二进制数
机器语言
汇编语言
高级语言

'''

# 6.python解释器版本特点，如何实现多版本共存

'''
确保不同版本解释器的python.exe所在的路径在环境变量中
复制重命名python.exe文件名
'''

# 7.常⻅的编程软件有哪些，你更倾向于哪个简单说说缘由

'''
pycharm，vscode，cmd
'''

# 8.什么是注释，python中如何编写注释

'''
注释就是对运行代码的解释，增强代码可读性

'''

# 9.什么是变量、如何定义变量、阐述内部本质

'''

'''

# 10.变量的命名规范与命名⻛格

'''
数字，字母，下划线组成
不能以数字开头
不能以关键字起名字
'''

# 11.什么是垃圾数据，简单聊聊python中的垃圾回收机制

'''
垃圾数据就是用不到的数据
垃圾回收机制是pycharm自带的一种机制
引用计数：当引用计数为0的时候，这些数据就会被回收
标记清除：主要是解决循环引用，当一条数据没有从栈发出，我们就会给他标记一下，方便下次清除他
分代回收：为了解决效率问题，每次大排查太消耗资源，分代去清理
'''

# 12.列举你所知道的python基本数据类型及各⾃表现形式

'''
布尔值 True/False   1,0,'',[],{},
整型 int  
浮点型 float
字符串 string
列表 list
元组 tuple
字典 dictionary
集合 set
'''

# 1.
# 编写⽤户识别程序
# 要求:
# 可循环根据⽤户输⼊的姓名不同输出不同的身份信息
# 添加程序结束功能(如⽤户输⼊字⺟q直接结束识别程序)
# jason: 扫地僧
# tony: 洗碗⼯ kevin: 服务员
# jack: 配菜员
# 其他:
# 未识别

'''
staff_dic={'jason': '扫地僧','tony': '洗碗⼯','kevin': '服务员','jack': '配菜员'}

print('''
# 1,识别功能
# 2,结束功能
''')
while True:
    choice =  input('请输入编号>>:').strip()
    if choice =='1':
        username = input('请输入您的姓名>>:').strip()
        if username :
            if username in staff_dic:
                print(staff_dic[username])
            else:
                print('未识别')
        else:
            print('输入不能为空')
    elif choice =='2':
        break
    else:
        print('输入有误')
'''

# 2.
# 利⽤for循环及range⽅法⾃动⽣成链家⼆⼿房多⻚数据⽹址(⼗条以
# 上即可)
# 初始⽹址: https://sh.lianjia.com/ershoufang/

'''
# https://sh.lianjia.com/ershoufang/pg1/
# https://sh.lianjia.com/ershoufang/pg2/

base_url = 'https://sh.lianjia.com/ershoufang/pg%s/'
for i in range(20):
    print(base_url %i )

'''

# 3.
# 编写⽤户登录程序
# 温馨提示:
# ⽤户名与密码来源于字符串source_data = 'jason|123'
# 想办法从中拆分出⽤户名和密码⽤于后续账户信息⽐对
# 普通要求:
# 1.
# 验证失败情况下可⼀直循环验证
# 成功则直接退出
# 拔⾼练习:
# 1.
# 只允许三次失败机会
# 2.
# 登录成功后进⼊内层循环，⽤户输⼊任何指令利⽤格式化输出
# 打印正在执⾏该⽤户指令即可，直到⽤户输⼊字⺟q退出内层循环
# Author: JasonJi

'''
source_data = 'jason|123'
count=1
while count<4 :
    username = input('请输入您的用户名>>:').strip()
    password = input('请输入您的密码>>:').strip()
    name, pwd = source_data.split('|')
    if username and password:
        if username == name and password == pwd:
            print('登录成功')
            break
        else:
            print('用户名或者密码错误,还剩%s次数尝试机会'%(3-count))
            count += 1
    else:
        print('输入的信息不能为空')
'''

# 1.尽可能多的列举python字符串类型操作⽅法(⽅法名称 + 功能介绍)

'''
去除字符串头尾指定的字符（默认是空格）	strip
切分指定字符(结果是一个列表)	split
统计字符串字符个数	count
大小写转换	upper/lower
字符串的拼接	join
判断字符串开头或者结尾	startswith/endswith
字符串替换（可以指定替换字符个数）	replace
'''

# 2.尽可能多的列举python列表类型操作⽅法(⽅法名称 + 功能介绍)

'''
增：
append 在尾部追加一个元素
insert 在指定索引插入一条数据
extend 一次性添加多个元素

删：
pop 有返回值 可以通过索引删除元素，默认最后一个元素
remove 删除指定元素
clear 清空
del 删除指定索引的值

改：

查：

其他：
len() 计算长度
count 计数
'''

# 3.诠释什么是可变类型与不可变类型

'''
可变类型（不可hash）：就是通过内置方法修改值的时候，内存地址没有发生改变，id值没有发生改变，改变的是原值，说明该数据类型可变（字典，集合，列表）
不可变类型（可hash）：就是通过内置方法修改值的时候，内存地址发生改变，id值发生改变，改变的不是原值，产生新的值,说明该数据类型不可变（元组，字符串）
'''

# 4.什么是队列与堆栈，能否⽤列表模拟⼀下各⾃特征

'''

'''

# 5.尽可能多的列举python字典类型操作⽅法(⽅法名称 + 功能介绍)

'''

统计列表中数据值的个数	len
通过key值，有则改之，无则填之	
通用删除，通过key删除对应的值	del
通过key删除对应的值	pop
获取字典所有的k值 结果当成是列表即可	keys
获取字典所有的v值 结果当成是列表即可	values
修改 键存在则是修改 键不存在则是新增	update



'''

# 6.请⽤尽可能完整的语⾔表示出元组极其特点

'''
不可变类型，有序，可重复
'''

# 7.请⽤尽可能完整的语⾔表示出集合并说说它所具备的功能

'''
去重
成员运算
'''

# 8.什么是字符编码，能否说说他的来⻰去脉

'''
ASCII
utf-8
unicode
'''

# 9.字符编码的实际应⽤有哪些

'''

'''

# 10.什么是⽂件，python中如何操作⽂件

'''

'''

# 11.⽂件的读写模式有哪些，各⾃有何特点

'''
r模式打开的文件只读模式(默认模式)，不存在直接报错
w模式打开的文件只写操作，文件路径存在:w模式会先清空该文件内容,然后等待填写新内容,不存在则自动创建该文件
a模式打开的文件默认是在末尾追加新的内容文件路径存在:a模式不会清空该文件内容,只在文件末尾等待填写新内容,不存在则自动创建该文件

'''

# 12.⽂件的操作模式有哪些，各⾃有何特点

'''
t模式(文本模式) 1.只能操作文本文件2.必须指定encoding参数3.读写都是以字符串为单位	
rt
wt
at

b模式(二进制模式) 必须指定模式不能省略rb wb ab1.能够操作所有类型的文件2.不需要指定encoding参数3.读写都是以bytes为单位	
rb
wb
ab
'''

# 13.⽂件常⽤操作⽅法有哪些

'''
一次性读取文件内容	read()
读取一行内容	readline( )
以行的方式读取所有内容并以列表返回['第一行\n','第二行\n']	readlines( )
填写文件内容	write( )
支持填写容器类型多个数据值	writelines( )

'''

# 14.什么是函数，定义函数的语法结构及各部分含义

'''

函数是盛放代码的容器
如果我们重复实现某一功能，直接把实现这一功能的代码丢到一个函数内
使用函数的原因：为了解决代码冗余,增强程序的可读性

语法
def 函数名(参数):
    """函数注释"""
    函数体代码
    return 返回值

def: 定义函数的关键字；
函数名：函数的功能的名字；
括号：括号内定义参数，可有可无的；
冒号：括号后要加冒号；
函数注释: 描述函数功能，增强函数的可读性；
函数体：逻辑代码；
return 值：定义函数的返回值，return是可有可无的。

定义函数：只检测函数体语法不不执行函数体代码

'''


# 一、
# 编写员⼯管理系统
# 功能要求:
# 1.
# 添加员⼯信息
# 提示: 编号(不能重复)、姓名、年龄、薪资
# 2.
# 查询特定员⼯
# 提示: 根据编号查找
# 展示结构⽤格式化输出美化
# 3.
# 修改员⼯薪资
# 提示: 先根据编号查找之后再修改薪资
# 4.
# 查询所有员⼯
# 提示: 循环⼀⾏⾏展示
# 5.
# 删除特定员⼯
# 提示: 根据编号确定


#
# info = {}
#
# def add_staff():
#     id = input('请输入您的编号>>:').strip()
#     if id:
#         if id not in info:
#             info[id]={}
#             username = input('请输入您的用户名>>:').strip()
#             age = input('请输入您的年龄>>:').strip()
#             salary = input('请输入您的薪资>>:').strip()
#             if username and age and salary:
#                 info[id][id]=id
#                 info[id]['姓名']=username
#                 info[id]['年龄']=int(age)
#                 info[id]['薪资']=int(salary)
#                 print(info)
#             else:
#                 print('输入信息不能为空')
#         else:
#             print('编号已存在')
#     else:
#         print('编号不能为空')
#
# def check_one_staff():
#     id = input('请输入您的编号>>:').strip()
#     if id:
#         if id in info:
#             print(f'''
#                     --------------------info------------------
#                         编号:{info[id][id]}
#                         姓名:{info[id]['姓名']}
#                         年龄:{info[id]['年龄']}
#                         薪资:{info[id]['薪资']}
#                     ------------------------------------------
#             ''')
#         else:
#             print('编号不存在')
#     else:
#         print('编号不能为空')
#
# def change_staff():
#     id = input('请输入需要修改薪资的员⼯编号>>:').strip()
#     if id:
#         if id in info:
#             salary = input('请输入薪资>>:').strip()
#             info[id]['薪资'] = int(salary)
#         else:
#             print('编号不存在')
#     else:
#         print('编号不能为空')
#
#
# def check_all_staff():
#     all_staff = info.values()
#     for staff in all_staff:
#         print(
#         f'''
#                 --------------------info------------------
#                     编号:{staff.get('id')}
#                     姓名:{staff.get('姓名')}
#                     年龄:{staff.get('年龄')}
#                     薪资:{staff.get('薪资')}
#                 ------------------------------------------
#         ''')
#
# def del_staff():
#     id = input('请输入需要删除的员⼯编号>>:').strip()
#     if id:
#         if id in info:
#             del info[id]
#         else:
#             print('编号不存在')
#     else:
#         print('编号不能为空')
#
# def out():
#     exit()
#
#
# command_dict = {
#     '1': ['添加员⼯信息', add_staff],
#     '2': ['查询特定员⼯', check_one_staff],
#     '3': ['修改员⼯薪资', change_staff],
#     '4': ['查询所有员⼯', check_all_staff],
#     '5': ['删除特定员⼯', del_staff],
#     '6': ['退出', out],
# }
#
# while True:
#     for command in command_dict:
#         print(command,command_dict[command][0])
#     choice = input('请输入您要执行的指令>>:').strip()
#     if choice in command_dict:
#         command_dict[choice][1]()
#     else:
#         print('输入有误')


# 2.
# 基于⽂件实现⽤户注册及登录功能
# 普通要求:
# 单⽤户模式
# 并且注册登录功能⽆需整合
# 进阶要求:
# 单⽤户模式
# 注册登录功能可循环执⾏
# 拔⾼要求:
# 多⽤户模式
# 注册登录功能可循环执⾏

'''
import os

def register():
    username = input('请输入您的姓名>>:').strip()
    with open(file_name,'r',encoding='utf8')as f:
        for line in f:
            real_name = line.split(',')[0]
            if username == real_name:
                print('用户名已存在')
                break
        else:
            password = input('请输入您的密码>>:').strip()
            print('%s注册成功' %username)
            info_data = username + ',' + password + '\n'
            with open(file_name,'a',encoding='utf8')as f:
                f.write(info_data)
def login():
    username = input('请输入您的姓名>>:').strip()
    with open(file_name, 'r', encoding='utf8') as f:
        for line in f:
            password = input('请输入您的密码>>:').strip()
            real_name, real_pwd = line.split(',')
            if username == real_name and password == real_pwd.rstrip('\n'):
                print('登录成功')
                break
        else:
            print('用户名或者密码错误')
def out():
    exit()
command_dic = {
    '1': ['注册',register],
    '2': ['登录',login],
    'q': ['退出',out]
}

def main_entrance():
    while True:
        for command in command_dic:
            print(command,command_dic[command][0])
        choice = input('请输入编号>>:').strip()
        if choice:
            if choice in command_dic:
                command_dic[choice][1]()
        else:
            print('输入有误')

file_name = 'a.txt'
if __name__ == '__main__':
    if os.path.exists(file_name):
        pass
    else:
        with open(file_name, 'a', encoding='utf-8') as f:
            pass

    main_entrance()
'''


