import socket
import sys
import time

server_socket=socket.socket()
server_host=socket.gethostname()
server_ip=socket.gethostbyname(server_host)
port=1234

server_socket.bind((server_host, port))
print("Binding Successful!")
print("This is your IP:",server_ip)

server_name=input("Enter name:")
server_socket.listen(1)

client_object, address=server_socket.accept()
print("Recieved connection from", address[0])
print("Connection Established. Connected From:",address[0])

client_name=(client_object.recv(1024)).decode()
print(client_name,"has connected")
client_object.send(server_name.encode())

while True:
    message=input("Me:")
    client_object.send(message.encode())
    message=(client_object.recv(1024)).decode()
    print(client_name,":",message)

client_object.close()
server_socket.close()
