import socket

s=socket.socket()
s.bind(("127.0.0.1",1237))
s.listen()
c, add = s.accept()
c.send("Enter OTP".encode())
otp=c.recv(1024).decode()
if otp  == '8894':
    c.send("You are authenticated".encode())
    data=c.recv(1024).decode()
    print("Client:",data)
    data=input("Enter Text:")
    c.send(data.encode())
else:
    c.send("You are not authenticated".encode())
c.close()
s.close()