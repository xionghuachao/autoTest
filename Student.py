
list = ["黑马", "哈哈", "什么"]
def while1(i) :



 while i< len(list) :
     print(list[i])
     i+=1
while1(0)
def list1() :
    for a in list :
        print(a)
list1()
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def asa() :

    i=0;
    while i<len(list_1) :
        if list_1[i]%2==0 :
            print(list_1[i])
        i+=1
asa()
def for_1() :
    for e in list_1 :
        if e%2==0 :
            print(e)
for_1()
#定义元组
t1=(1,"Hello",True)
t2=()
#定义空元组
t3=tuple()
print(t3)
#定义单个元素的元素
te=("hello")
#元组的嵌套
t5=((1,2,3),(4,5,6))
#下标索引取出内容
print(t5[1][2])
#index
index=t1.index(1)
print(index)
#count的统计方法
t7=("haha","哈哈","haha")
count=t7.count("haha")
print(count)
#元组的遍历while
index=0
while index<len(t7) :
    print(t7[index])
    index+=1
#元组的遍历for
for index in t7 :
    print(index)
#元组内容不可以修改，可以嵌套LIST
t9=(1,2,[4,5,6])
t9[2][0]="kan"
print(t9)
tt=("周杰伦",11,["football","music"])
inte=tt.index(11)
print(inte)
print(tt[0])
del tt[2][0]
print(tt)
tt[2].append("coding")
print(tt)
#字符串
my_str="itheima an icah"
#通过下表索引
value=my_str[3]
#index方法,找到下标索引值
print(my_str.index("t"))
#replace方法
my=my_str.replace("a","b")
print(my)
#split方法
my=my_str.split(" ")
print(my)
#去掉空格strip
muu=my_str.strip("an")#去掉前后字符
print(muu)
#统计字符串中某字符的个数
print(my_str.count("a"))
#统计字符串的长度
print(len(my_str))
