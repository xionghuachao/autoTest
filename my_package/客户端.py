import socket


socket_client=socket.socket()
socket_client.connect(("localhost",8888))
socket_client.send("你好".encode("UTF-8"))
data=socket_client.recv(1024)
print(f"客户端回复信息{data.decode('UTF-8')}")
socket_client.close()