# #打开文件，不存在文件，自动穿创建文件，文件存在，会清除之前的内容
# f=open("D:/test.txt","w",encoding="utf-8")
# #写入
# f.write("helloword")#写入内存中
# f.flush()#写到文件中
# f.close()
# #打开一个存在的文件
# f=open("D:/test1.txt","a",encoding="utf-8")
# #写入
# f.write("\n黑马程序员")#写入内存中
# f.flush()#写到文件中
# f.close()
f=open("D:/b1.txt","r",encoding="utf-8")

e=open("D:/bill.txt.bak","w",encoding="utf-8")
for line in f :
    line=line.strip()
    if line.split(",")=="测试" :
        continue
    e.write(line)
    e.write("\n")
e.close()
f.close()




