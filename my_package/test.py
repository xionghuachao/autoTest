# #设计一个类，
# class Student :
#     name=None
#     gender=None
#     native=None
#     age=None
# #创建一个对象（类比生活中，打印一张登记表）
# student=Student()
# #对象属性进行赋值（类比生活中，填写表单）
# student.age=18
# student.name="小红"
# #获取对象中记录的信息
# print(student.age)
import self as self
from trio._abc import Clock
#
#
# class Student :
#     name=None
#     age=None
#     def say_hi(self,name):
#         print(f"你好{self.name}")
#
# student=Student()
# student.name="张"
# student.say_hi("张三")
#构造方法
#演示构造方法对成员变量赋值
#构造方法的名称__init__
class Student :
    age=None
    name=None
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{name}")

if __name__ == '__main__':
    student=Student("小明","22")


