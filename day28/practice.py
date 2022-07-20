import requests
import re

res = requests.get('http://www.redbull.com.cn/about/branch')
with open('company.html','wb')as f:
    f.write(res.content)
with open('company.html','r',encoding='utf8')as f:
    data = f.read()
company_name_list = re.findall('<h2>(.*?)</h2>', data)
company_addr_list = re.findall("<p class='mapIco'>(.*?)</p>", data)
company_email_list = re.findall("<p class='mailIco'>(.*?)</p>", data)
company_phone_list = re.findall("<p class='telIco'>(.*?)</p>", data)
res = zip(company_name_list, company_addr_list, company_email_list, company_phone_list)
from openpyxl import Workbook
wb = Workbook() # 创建excel文件
wb1 = wb.create_sheet('红牛分公司信息', 0)
wb1.append(['公司名称','公司名称','公司邮箱','公司电话'])
for i in res:
    wb1.append(i)
wb.save(r'红牛分公司.xlsx')























