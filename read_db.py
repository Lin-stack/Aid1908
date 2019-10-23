'''
read_db.py
pymysql 读操作演示
'''


import pymysql

#连接数据库
db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    database = 'stu',
    charset = 'utf8'
)

#生成游标对象 （操作数据库，执行sql语句）
cur = db.cursor()

# name = input('请输入名字：')
#执行读操作
#sql = "select name,age from class1 where sex='m';"
# sql = "select * from class1 where name = '%s';"% name
# cur.execute(sql) #执行语句

#class1中查询性别为m 分数大于85
sql = "select * from class1 where sex=%s and score>%s;"
#通过execute第二个参数列表传参给sql语句
cur.execute(sql,['m',85])


# 迭代cur获取查询结果
# for i in cur:
#     print(i)

#获取一个查询结果
# one_row = cur.fetchone()
# print(one_row)

#获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)


#获取所有的查询结果
all_row = cur.fetchall()
print(all_row)


#关闭游标和数据库连接
cur.close()
db.cursor()