# This is a sample Python script.
import abc
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, '+name)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

print_hi("pycharm")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# age=input("请输入年龄")
# age=int(age)
# if age>18 :
#     print("您已成年")
# elif age<18 :
#     print("xiaoyu")
# else:
#     print("未成年")
# print("祝您游玩愉快")
# num=5
# if int(input("请输入第一次猜的数字"))==num :
#     print("猜对了")
# elif int(input("猜错了"))==num:
#       print("再猜一次")
# elif int(input("猜错了"))==num:
#       print(f"最后一次{num}")
# if  int(input("你的身高是多少"))>120 :
#     print("身高超出限制")
#     if int(input("你的vip等级"))>3 :
#         print("可以玩耍")
#     else :print("等级不够")
# else :
#    print("身高不够")


# if  18<=int(input("请输入年龄"))<30  :
#     if int(input("入职时间"))>2 :
#         print("可以领取")
#     elif int(input("级别"))>3 :
#         print("可以领取")
#     else : print("年龄或级别不满去")
# else :
#     print("年龄不够")
# num=random.randint(1,10)
# print(num)
# guess=int(input("猜测的数字"))
# if guess==num :
#     print("猜对了")
# else  :
#     if guess > num:
#       print("猜大了")
#     elif guess < num:
#       print("猜小了")
# s=0
# i=1
# while i<=100:
#    s=s+i
#    i+=1
# print(s)
# s=True
# num=random.randint(1,100)
# count=0
#
# while s :
#     guess = int(input("请猜测数字"))
#     count += 1
#     if guess==num :
#
#         print("猜对了")
#         s=False
#     else :
#         if guess>num :
#             print("猜大了")
#         else :
#             guess<num
#             print("猜小了")
# print(f"总共猜测{count}")
i=1
while i<=20 :
    print(f"第{i}天")

    j=1
    while j<10 :
        print(f"第{i}朵")
        j+=1
    i += 1
print(f"表白{i-1},收到{j}朵")
#输出自动给换行-输出到一行
# print("hello",end='')
# print("word" )
#\t制表符，对其字母相当于tab
print("hello\tword")
#换行
# print()
# count=0
# name="itheima is a brand of itcast"
# for i in name:
#     if(i=="a") :
#         count+=1
# print(count)
# for x in range(5,10):
#     print(x)
#
#
# count=0
# x=1
# for x in range(1,100):
#     if(x%2==0) :
#         count+=1
# print(x)
# print(count)
# num=random.randint(1,11)
# count_1=10000
# for i in range(1,21) :
#     if num<5 :
#         print(f"{i}不发工资")
#         continue
#     if 5<num<=10 :
#         count_1=count_1-1000
#         print(f"{i}账户余额{count_1}")
#
#         if count_1==0 :
#           print("当前余额不足")
#         break
# # print(count_1)
str1="aavc"
str2="abcdr"
str3="python"
# count=0;
# for i in str1:
#     count+=1
# print(count)
# print(len(str2))

def my_len(data):
    count=0;
    for i in data :
        count+=1
    print(f"{data}的长度{count}")
my_len(str1)
my_len(str2)
my_len(str3)
def say_hi():
    return 1
print(say_hi())
def h():
    print("和网速")
h()
def add(x,y) :
    """
    多行注释
    :param x: 相加的一个参数
    :param y: 相加的一个参数
    :return:
    """
    result=x+y
    return None
def fun_1() :
    print("abc")
    add(2, 3)
fun_1()
r=add(2,3)
print(r)
#无返回值
s=None
print(type(s))
#global

def testa() :
    global num;
    num=2
    print(num)
# #print(num)
# money=50000
# name=None
# name=input("输入姓名")
# def query(show):
#     if show :
#         print("查询余额")
#     print(f"{name},{money}")
# def saving(num):
#     global money
#     money+=num
#     print("存款成功")
#     query(False)
# name={1,2,3,4}
# for i in name :
#     print(i)
# list=["ithaa","avc",123,True]
# list1=[[1,2],[1,3]]
# print(list1[0][1])
# print(list[0])
# print(list[-1])#倒数第一个
# print(type(list))
# list.append(3)
# #查找元素下标
# list.index(123)
# #修改特定下标列表的值
# list[0]=56
#
# #在指定位置进行插入
# list.insert(1,"hah")
# #追加元素在尾部
# #list.append("和好")
# print(list)
# #在列表后边追加一个新的列表
# list11=[1,3,5]
# list.extend(list11)
# #删除元素
# list.remove("hah")
# #通过pop取出元素
# #element=list.pop("和好")
# #清空列表内容
# list.clear()
# #统计内元素的数学
# list.len
# #统计某元素的数量
# list.count(123)
list=[21,25,21,23,22,20]
list.append(31)
print(list)
list1=[29,33,30]
list.extend(list1)
print(list)
print(list[0])
print(list[-1])
print(list.index(31))
print(list)










