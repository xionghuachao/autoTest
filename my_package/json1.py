import json
#准备列表，列表内每一个元素都是字典，将其转换成JSON
data=[{"name":"老王","age":"15"},{"name":"老李","age":"18"},{"name":"老大","age":"12"}]
#准备列表字典，将字典转为为JSON
json_str=json.dumps(data,ensure_ascii=False)
print(json_str)
#将Json字符串转换为python数据类型
s='[{"name":"老王","age":"15"},{"name":"老李","age":"18"},{"name":"老大","age":"12"}]'
str=json.loads(s)
print(str)
#将json字符串转换为PYTHON数据类型
se='{"name":"老大","age":"12"}'
st=json.loads(se)
print(type(st))