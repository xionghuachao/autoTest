#返回多个返回值
__all__=['test_return']
def test_return() :
    return 1,2
x,y=test_return()
print(x)
print(y)

def user(name,age) :
    print(f"{name}+{age}")
#位置参数
user("男",12)
#关键字参数
user(age=10,name="gender")
#缺省参数默认参数要写到最后面
def user_info(name,age,gender="男"):
    print(f"{name}+{age}+{gender}")

#位置不定长
def user_info(*args):
    se=str(args)
    print(se)

#关键字不定长
def user_info(**kwargs):
    se=str(kwargs)
    print(se)
user_info(name="小王",age=1)
#定义一个参数，函数作为参数,compute是函数
def  test(compu) :
    result=compu(1,2)
    print(result)


#定义一个函数，准备作为参数传入另一个函数
def compu(x,y) :
    return x-y;
#调用函数

test(lambda x,y:x+y)
if __name__ == '__main__':
  user_info("小米", 12, "女")
