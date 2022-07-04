# 阶乘
def factorial(new_num):
    result = 1
    while new_num > 0:
        result *= new_num
        new_num -= 1
    return result


number = input('请输入您需要计算的阶乘>>:').strip()
print(number)
new_num = int(number)
print(factorial(new_num))

# 圆的面积
import math


def circle_area(r):
    result = math.pi * r ** 2
    return round(result, 2)


num = input('请输入圆的半径>>:').strip()
r = ''.join(num)
r = int(r)
print(circle_area(r))


# 计算数字范围中所有的偶数


# 方法一：

def even_number(begin, end):
    even_list = []
    for i in range(begin, end):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


number1 = input('请输入开始值>>:').strip()
number2 = input('请输入结束值>>:').strip()

begin = ''.join(number1)
end = ''.join(number2)
if begin and end:
    print(even_number(int(begin), int(end)))
else:
    print('输入不能为空')

# 方法二：

number1 = input('请输入开始值>>:').strip()
number2 = input('请输入结束值>>:').strip()

begin = ''.join(number1)
end = ''.join(number2)
if begin and end:
    even_numbers = [i for i in range(int(begin), int(end)) if i % 2 == 0]
    print(even_numbers)
else:
    print('输入不能为空')


# 列表推导式的语法格式如下：
# [表达式 for 迭代变量 in 可迭代对象[ if 条件表达式]]

# 移除列表中的多个元素

# 方式一：

def remove_multi_element(raw_list, remove_element):
    for i in remove_element:
        raw_list.remove(i)
    return raw_list


raw_list = input('请输入原始列表数据>>:').strip().split(',')
remove_element = input('请输入要移除的元素>>:').strip().split(',')
print(remove_multi_element(raw_list, remove_element))

# 方式二：
raw_list = input('请输入原始列表数据>>:').strip().split(',')
remove_element = input('请输入要移除的元素>>:').strip().split(',')
data = [element for element in raw_list if element not in remove_element]
print(data)

# 实现学生成绩排序
stu_list = [
    {'sno': 101, 'sname': '小张', 'sgrade': 88},
    {'sno': 102, 'sname': '小王', 'sgrade': 77},
    {'sno': 103, 'sname': '小李', 'sgrade': 99},
    {'sno': 104, 'sname': '小赵', 'sgrade': 66}
]
new_stu_list = sorted(stu_list, key=lambda x: x['sgrade'])
# for循环前面的数据,依次交给后面的匿名函数处理 将返回值当做操作条件
print(
    new_stu_list)  # [{'sno': 104, 'sname': '小赵', 'sgrade': 66}, {'sno': 102, 'sname': '小王', 'sgrade': 77}, {'sno': 101, 'sname': '小张', 'sgrade': 88}, {'sno': 103, 'sname': '小李', 'sgrade': 99}]

# 读取成绩文件排序数据

s_id = input('请输入您的学号>>:').strip()
s_name = input('请输入您的姓名>>:').strip()
s_score = input('请输入您的成绩>>:').strip()
s_info = s_id + ',' + s_name + ',' + s_score + '\n'
with open('student_info.txt', 'a', encoding='utf-8') as f1:
    f1.write(s_info)
with open('student_info.txt', 'r', encoding='utf-8') as f2:
    sort_list = []
    for line in f2:
        new_line = line.rstrip('\n').split(',')
        sort_list.append(new_line)
    sort_stu_info = sorted(sort_list, key=lambda x: int(x[2]))
    print(sort_stu_info)

# 统计学生最高分最低分平均分
s_id = input('请输入您的学号>>:').strip()
s_name = input('请输入您的姓名>>:').strip()
s_score = input('请输入您的成绩>>:').strip()
s_info = s_id + ',' + s_name + ',' + s_score + '\n'
with open('student_info.txt', 'a', encoding='utf-8') as f1:
    f1.write(s_info)
with open('student_info.txt', 'r', encoding='utf-8') as f2:
    sort_list = []
    for line in f2:
        new_line = line.rstrip('\n').split(',')
        sort_list.append(new_line)
    score = [int(i[2]) for i in sort_list]
    print(max(score), min(score), round(sum(score) / len(score)))

# 统计英语文章每个单词出现的次数
with open('artical.txt', 'r', encoding='utf-8') as f:
    word_dict = {}
    for line in f:
        # word = line[:-1].split()
        words = line.rstrip('\n').split()
        print(words)
        for word in words:
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1
print(word_dict)
