#打开文件
import time

f=open("D:/网盘下载使用教程.txt","r",encoding="utf-8")

#读取文件read()读取全部内容
line=f.read()
print(line.count("一"))
f.close()
#读取文件readlines
# lins=f.readlines()#读取文件的全部行,封装到列表里面
# print(lins)
#读取文件readline
# lins=f.readline()#读取一行数
# print(lins)
#for循环读取文件
# for line in f:
#     print(line)
# #文件的关闭
# time.sleep(3000)
# f.close()
#with open 语法操作文件,可以自动关闭文件
# with open("D:/网盘下载使用教程.txt","r",encoding="utf-8") as f :
#     for line in f:
#         print(f"每一行数据{line}")
