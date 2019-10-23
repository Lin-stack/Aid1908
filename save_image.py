'''
存储二进制文件演示
'''

import pymysql

#连接数据库
db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    database = 'books',
    charset = 'utf8'
)

#生成游标对象 （操作数据库，执行sql语句）
cur = db.cursor()


#存储图片
# with open('12.jpg','rb') as f:
#     data = f.read()
#
# try:
#     sql = "insert into image values(1,%s,%s);"
#     cur.execute(sql,['12.jpg',data])
#     db.commit()
# except:
#     db.rollback()

#读取图片
sql = "select filename,img from image where filename='12.jpg';"
cur.execute(sql)
data = cur.fetchone()
with open(data[0],'wb') as f:
    f.write(data[1])

#关闭游标和数据库连接
cur.close()
db.cursor()