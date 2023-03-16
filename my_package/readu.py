import xlrd
from pymysql import Connection
FilePath = 'D:/StudentInfo1.xls'

# 1.打开excel文件
wkb = xlrd.open_workbook(FilePath)
# 2.获取sheet
sheet = wkb.sheet_by_index(0)  # 获取第一个sheet表['学生信息']
# 3.获取总行数
rows_number = sheet.nrows
# 4.遍历sheet表中所有行的数据，并保存至一个空列表cap[]
cap = []
for i in range(rows_number):
    x = sheet.row_values(i)  # 获取第i行的值（从0开始算起）
    cap.append(x)
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


for Stu in cap:
    Sno = int(Stu[0])
    Sname = Stu[1]
    Ssex = Stu[2]
    Sage = Stu[3]
    Sdept = Stu[4]
    cursor.execute(
        f"insert into student(Sno,Sname,Ssex,Sage,Sdept) value ({Sno},'{Sname}','{Ssex}',{Sage},'{Sdept}')")
conn.commit()
conn.close()
print("插入数据完成")
