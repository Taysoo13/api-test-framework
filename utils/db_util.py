import pymysql
def query(sql):
   conn=pymysql.connect(
       host="localhost",
       user="root",
       password="123456",
       database="school",
       charset="utf8"
   )
   # 拿游标
   cursor = conn.cursor()
   # 执行sql
   cursor.execute(sql)
   # 取结果
   return cursor.fetchall()
   conn.close()
   return result
def execute(sql):
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="school",
        charset="utf8"
    )
    cursor=conn.cursor()
    cursor.execute(sql)
    # 提交
    conn.commit()
    conn.close()




