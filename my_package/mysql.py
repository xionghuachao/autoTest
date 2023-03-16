#通过pymysql
from pymysql import Connection
#构建mysql数据库连接
conn=Connection(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    autocommit=True#自动提交
)
#执行非查询性质sql
cursor=conn.cursor() #获取游标对象
#选择数据库
conn.select_db("imooc")
#执行查询sql
# cursor.execute("create table test_py(id int);")
# cursor.execute("select * from student")
# su=cursor.fetchall()
# for i in su :
#     print(i)
cursor.execute("insert into student values(4, '小2', '女', '2020-01-02', '122333', null, '烦1烦烦');")
#conn.commit()
conn.close()
