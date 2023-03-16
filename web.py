from tokenize import String

from selenium  import webdriver;
from selenium.webdriver.common.by import By

666
13.14
s="11"
a=6666
print(s,"NI")
# 买一个冰激凌
money=50
s1=money-10
print(s1)
#每隔一小时输出一下钱包余额
money=50
b=10
k=5
#查看数据类型
print(type(k))
print("当前钱包余额",money)
print("购买了冰激凌",b)
print("购买了可乐",k)
print("钱包余额",money-b-k)
#类型数字转换
#a=int(s)# 转换成int
#print(type(a),s)
aa=float(s)# 转换成 float
print(type(aa),s)
#str(s) # 转换成 str
#driver=webdriver.Chrome()
#加载网页
#driver.get("https://www.baidu.com/")
#定位元素
#driver.find_element(By.ID,"kw")
it_1="黑马程序员"
ss=22
print(it_1+"%s" %(ss))
#占位符%s  整数：%d  小数%f
print(f"{it_1}{ss}")
name="传智播客"
code="003032"
price=19.99
factor=1.2
day=7
print(f"公司：{name},股票代码：{code},当前股价：{price}")
print("每日增长系数%.1f,经过%d天的增长后，股价达到了%.2f"%(factor,day,price*factor))
print("请告诉我你是谁")
name=input()
print("你是%s"%(name))
num=input("你的银行卡密码是")
num=int(num)
print("银行卡密码是%s"%(num))
print(type(num))
user=input("用户名称")
type_1=input("用户类型")
print(f"您好：{user},您是尊贵的{type_1}用户，欢迎您光临")
age=10
if age>3:
    print("haha")

