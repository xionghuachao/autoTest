# 基础数据类型注解
import json
import random
from typing import Union

var_1: int = 10
var_2: str = "as"


# 类对象类型注解抽象类,抽象方法
class Student:
    def speck(self):
         pass


stu: Student = Student()
# 基础容器类型注解
my: list[int] = [1, 2, 3]
tuple1: tuple[int] = (1, 2, 3)
my_dict: dict[str,Union[int,str] ] = {"itheima": 666}

#返回类型注解
def ser(data:int)->int:
    print(type(data), data)


# 在注释中进行类型注释
var_1 = random.randint(1, 10)  # type:int
# json转成字典
var_2 = json.loads('{"name":"haha"}')  # type:dict[str,str]
print(type(var_2))
# 类型注释的限制
ser()
#联合类型

