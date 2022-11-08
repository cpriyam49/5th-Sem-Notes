import socket

c = socket.socket()
c.connect(("127.0.0.1",1237))
data=c.recv(1024).decode()
print(data, end=" ")
otp=input()
c.send(otp.encode())
data=c.recv(1024).decode()
print(data)
if data == "You are authenticated":
    data = input("Enter Text:")
    c.send(data.encode())
    data=c.recv(1024).decode()
    print("Server:",data)
else:
    c.close()