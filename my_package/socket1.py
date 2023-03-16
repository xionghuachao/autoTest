import socket
#创建socket对象
socket_server=socket.socket()
#绑定ip和地址端口
socket_server.bind(("localhost",8888))
#监听端口
socket_server.listen(1)
#listen方法内接受一个整数传参
conn,address=socket_server.accept()
#accept返回的是二元元组
print(f"接受到客户端信息{address}")
#接受客户端信息
data=conn.recv(1024).decode("UTF-8")
print("客户段发来的信息是",data)
msg=input("请输入客户端回复消息").encode("UTF-8")
conn.send()
conn.close()
socket_server.close()


