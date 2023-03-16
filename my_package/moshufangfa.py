class Student :
    name=None
    age=None
    address=None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address=address
#__str__相当于java的tostring,可以自动打印
    def __str__(self):
        return f"{self.age},{self.name},{self.address}"
stu=Student("xiao",23,"haha")
print(stu)
#__lt__魔术方法小于符号的比较print(stu1<stu2)
class Student :
    name=None
    age=None
    address=None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address=address

    def __lt__(self, other):
        return self.age<other.age

    # __le__魔术方法小于符号的比较print(stu1<=stu2)
    def __le__(self, other):
        return self.age < other.age

    # __eq__两个对象是否相等
    def __eq__(self, other):
        return self.age==other.age
stu1=Student("xiao",23,"haha")
stu2=Student("xi",25,"ha")
print(stu1<stu2)
print(stu1<=stu2)




