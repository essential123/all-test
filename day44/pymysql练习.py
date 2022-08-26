import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='db5',
    charset='utf8mb4',
    autocommit=True
)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql1 = 'select * from class'
cursor.execute(sql1)
res =cursor.fetchone()
print(res)
cursor.scroll(1,mode='absolute')
res=cursor.fetchone()
print(res)