import re
import os
s="python pythonitheima"
#match从头匹配
result=re.match("python",s)
print(result)
#serach搜索匹配
result=re.search("python",s)
print(result)
#findall搜索全部匹配
result=re.findall("python",s)
print(result)
s="itheima1 @pthon2 !!!666 #itcast3"
result=re.findall(r'\d',s)#字符串前面带上r表示转义无效
print(result)
#\W匹配非单词字符
result=re.findall(r'\W',s)
print(result)
#找出全部的英文字母
r='^[0-9a-zA-Z]{6,10}'#只能是字母数字，满足6-10位
s='1234567aB'
print(re.findall(r,s))
#匹配纯数字
s='11.9'
e='^[1-9][0-9]{1,10}$'
print(re.findall(e,s))
#匹配邮箱
r='^[\w-]+(\.)$'
def test_os():
    print(os.listdir("D:/Q"))#列出路径下内容
    print(os.path.isdir("D:/Q"))  # 列出路径下内容
    print(os.path.exists("D:/Q"))  # 列出路径下内容