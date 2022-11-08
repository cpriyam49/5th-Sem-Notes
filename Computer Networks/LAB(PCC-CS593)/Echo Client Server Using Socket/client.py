import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data="Hello, World"
s.send(data.encode())
data = s.recv(1024).decode()

print(f"Received ",data)