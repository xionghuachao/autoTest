str="itheima itcast boxuegu"
it=str.count("it")
print(it)
str1=str.replace(" ","|")
print(str1)
list=str1.split("|")
print(list)
#切片
my=[0,1,2,3,4]
result1=my[1:3]
print(result1)
my1=my[3:1:-1]
print(my1)
#元组切片
tup=(0,1,2,3,4,5,6)
tt=tup[0:7]
print(tt)
te=tup[::-1]
print(te)
#字符串切片,从0开始，步长为2，到最后结果
str1="0123445"
str3=str1[0:7:2]
print(str3)
#字符串切片，步长-1
str4=str1[::-1]
print(str4)
hh="万过薪月,员序程马黑来,nohtyP学"
h1=hh[::-1][9:14]

print(h1)
list1=hh.split(",")
list2=list1[1].replace("来","")[::-1]

print(list2)
#定义集合-无序-
set11={"船只教育","itheima","船只教育"}
#set_empty=set()#定义空集合
print(set11)
#print(set_empty)
#添加新元素
set11.add("python")
#移除元素
set11.remove("python")
#随机取出来一个元素
set11.pop()
#清空集合
set11.clear()
#取两个集合的插值
set1={1,2,4}

set2={2,4,6}
set3=set2.difference(set1)
print(f"set3={set3}")
#清除2个集合的差集
#set1.difference_update(set2)
print(set1)
#2个集合合并为1个
set4=set1.union(set2)
print(set4)
#统计集合数量
print(len(set1))
#集合的遍历,不能用while循环
for i in set1 :
    print(f"{i}")
my_list=["黑马程序员","传智播客","黑马程序员","传智播客","itcast","best"]
jh=set()
for i in my_list :
     jh.add(i)
print(jh)
#定义字典
map1={"王":99,"li":33}
map1.setdefault(1,2)
print(map1)
#定义空字典
#key值不能重复
map2={}
map3=dict()
#通过Key获取参数
print(map1.get("王"))
print(map1["王"])
#字典是可以嵌套的,可以嵌套数组和集合
ma1={"wang":{"语文":55,"数学":66},"李明":[22,55]}
print(ma1["wang"]["语文"])
#字典常用操作
my_dict={"周杰伦":99,"林俊杰":88,"张学友":90}
#新增元素
my_dict["张信哲"]=66
print(my_dict)
#更新元素
my_dict["周杰伦"]=80
print(my_dict)
#删除元素
#del my_dict["周杰伦"]
score=my_dict.pop("周杰伦")
print(score)
#清空元素
#my_dict.clear()
#print(my_dict)
#获取全部的key
su=my_dict.keys()
print(su)
#遍历字典
for i in my_dict :
    value=my_dict[i]
    print(f"{i}={value}")
for i in su :
    value=my_dict[i]
    print(f"{i}={value}")
#统计字典内的元素数量
print(len(my_dict))
my_dict1={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
          "周杰伦":{"部门":"市场部","工资":2800,"级别":2},
          "林俊杰":{"部门":"市场部","工资":3800,"级别":3}}
print(my_dict1)
s=1
for i in my_dict1 :
    ji=my_dict1[i]["级别"]-s
    my_dict1[i]["工资"]=ji*1000+ my_dict1[i]["工资"]
for name in my_dict1 :
    if my_dict1[name]["级别"]==1 :
        my=my_dict1[name]
        my["级别"]=2
        my["工资"]+=1000
        my_dict1[name]=my
print(my_dict1)
#max最大元素
max(my_dict1)
#min最小元素
min(my_dict1)
#类型转换
#list(my_dict1)
tuple(my_list)

#输入number = 123,输出321
del list
number1 = input('请输入一个三位数：')
liste = list(number1) #将输入的三位数的字符串存入列表
liste.reverse() #将列表元素反转
a = int(liste[0]) #取出反转后列表的元素并将其类型转为int类型
b = int(liste[1])
c = int(liste[2])  #也可以不反转列表，直接反着取出列表中的元素
re_number = a*100 + b*10 + c
print('%s的反转数是:%s'%(number1,re_number))
print('%d的反转数是:%d'%(int(number1),re_number))