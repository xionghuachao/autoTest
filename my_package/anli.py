
class Student :
    name=None
    age=None
    address=None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address=address
def f() :
 for i in range(1, 11):
    print(f"当前录入第{i}位学生信息，总共需要录入10位学生信息")
    name = str(input("请录入学生姓名"))
    age = int(input("请录入学生年龄"))
    address = str(input("请录入学生地址"))
    student = Student(name, age, address)
    print(f"学生{i}录入完成，信息为学生姓名{student.name},年龄{age},地址{address}")
f()


