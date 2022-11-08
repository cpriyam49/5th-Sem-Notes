import socket
import sys
import time

socket_server = socket.socket()
server_hostname = socket.gethostname()
server_ip = socket.gethostbyname(server_hostname)
port=1236

socket_server.bind((server_hostname, port))
print("Binding Successful")
print("This is Server\'s IP Address: ",server_ip)

socket_server.listen(1)

client_object, address=socket_server.accept()
print("Connection Established with Client.")
print("This is Client\'s IP Address: ",address[0])

client_object.close()
socket_server.close()
