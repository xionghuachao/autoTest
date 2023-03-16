from pymysql import Connection
from my_package import readu
conn=Connection(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    #autocommit=True#自动提交
)
#执行非查询性质sql
cursor=conn.cursor() #获取游标对象
#选择数据库

conn.select_db("imooc")
cursor.execute(f"insert into student(Sno,Sname,Ssex,Sage,Sdept) value ({readu.Sno},'{readu.Sname}','{readu.Ssex}',{readu.Sage},'{readu.Sdept}')")
conn.commit()
conn.close()
