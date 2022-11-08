import socket
import sys
import time

client_socket=socket.socket()
client_hostname=socket.gethostname()
client_ip=socket.gethostbyname(client_hostname)
port=1234

print("This is your IP address:",client_ip)
server_ip=input("Enter Server\'s IP address:")
client_name=input("Enter Client\'s name:")
client_socket.connect((server_ip, port))

client_socket.send(client_name.encode())
server_name = client_socket.recv(1024)
server_name = server_name.decode()
print(server_name,"has joined...")

while True:
    message=(client_socket.recv(1024)).decode()
    print(server_name,":",message)
    message=input("Me:")
    client_socket.send(message.encode())

client_socket.close()
