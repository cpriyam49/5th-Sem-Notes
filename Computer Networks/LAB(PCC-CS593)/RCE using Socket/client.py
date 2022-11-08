import socket

ip = socket.gethostbyname(socket.gethostname())
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
while True:
    command = input("Input : ")
    s.send(command.encode())
    if command == "exit":
        break
s.close()