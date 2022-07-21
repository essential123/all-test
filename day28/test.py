import re
# res = re.finditer('a','jason oscar aaa')
# print(res)
# for i in res:
#     print(i)

# res = re.match('a', 'aaa')
# print(res)
#
#
#

# obj = re.compile('a')
# print(re.findall(obj,'asjd21hj13123j'))
# print(re.findall(obj,'fdh3jh45jhqjha'))
# print(re.findall(obj,'asdasdadadasd'))

# findall针对分组的正则表达式匹配到的结果 优先展示
# res = re.findall('abc','abcabcabcabc')
# print(res) # ['abc', 'abc', 'abc', 'abc']
# res1 = re.findall('a(b)c','abcabcabcabc')
# print(res1)
#
# # findall也能够取消分组优先展示 (?:)
# print(res) # ['b', 'b', 'b', 'b']
# res = re.findall('a(?:b)c','abcabcabcabc')
# print(res)

# res = re.search('a(?P<id>b)(?P<name>c)','abcabcabcabc')
# print(res.group())
# print(res.group(1))
# print(res.group('id'))


# import re
# match = re.findall("(1\d+\|[a-z]+)","1234|asss|ZZZ|1345|adda")
# print(match)
#
# #输出：['1234|asss', '1345|adda']


# from openpyxl import Workbook
# wb = Workbook() # 创建excel文件
#
# wb1 = wb.create_sheet('成绩表')
# wb1.append(['age'])
# wb1.append([18,19,20])
#
# wb1['F11'] ='=sum(A2:C2)'
# from openpyxl import Workbook # 导入模块
#
# wb = Workbook() # 创建excel文件
#
# wb1 = wb.create_sheet('部门表', 0)
# wb1['A1'] = '财务部'
# wb1['B1'] = '开发部'
# wb1['C1'] = '研发部'
# wb1.cell(row=3, column=2, value='老六慢走')
#
# wb2 = wb.create_sheet('成员表')
#
# wb2.append(['username','age','gender','hobby'])
# wb2.append(['A',18,'male','read'])
# wb2.append(['B',18,'male','read'])
# wb2.append([None,18,'male',''])
#
# wb.save(r'company.xlsx')

# res = re.search('a(b)c','abcabcabcabc')
# print(res)
# print(res.group()) # abc
# print(res.group(0)) # abc
# print(res.group(1)) # b

