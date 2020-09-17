"""
数据库的写操作
"""
import pymysql
# 创建数据库连接
db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='stu',
    charset='utf8'
)
# 创建游标
cur=db.cursor()
# 操作数据库
try:
    name=input("Name:")
    age=input("Age:")
    gender=input("Gender:")
    score=input("Score:")
    newName=input("NewName:")
    # sql="insert into class_1 (name,age,gender,score)" \
    #     "values('%s','%s','%s','%s')"%(name,age,gender,score)
    # sql = "insert into class_1 (name,age,gender,score)"\
    # "values(%s,%s,%s,%s)"
    # cur.execute(sql,[name,age,gender,score])
    # 修改
    # sql="update class_1 set name=%s where name=%s"
    # cur.execute(sql, [newName,name])
    # 删除
    sql = "delete from class_1 where name=%s"
    cur.execute(sql, [name])

    db.commit()
except Exception as e:
    print(e)
    db.rollback()
# 关闭游标和数控
cur.close()
cur.close()