#
#from hanshu import user
from hanshu import *
from hanshu import user

try :
   f=open("D:/abc.txt","r",encoding="utf-8")
except :
    print("出现异常了，因为文件不存在，改为w模式")
    f = open("D:/abc.txt", "w", encoding="utf-8")
#捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
#捕获多个异常
try:
    print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常")
    print(e)
#未正确设置捕获异常，将无法捕获异常

#捕获所有异常
try:
   print("hello")
except Exception as e :
    print("出现异常了")
else  :
    print("没有异常")
finally:
    f.close()
#if __name__ == '__main__': 在同意文件写入调用可以显示，在其他文件写入，调用是可以不显示
test_return()


