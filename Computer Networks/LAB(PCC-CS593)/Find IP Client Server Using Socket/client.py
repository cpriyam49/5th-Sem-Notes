import socket
import sys
import time

socket_client = socket.socket()
client_hostname = socket.gethostname()
client_ip = socket.gethostbyname(client_hostname)
port=1236

# socket_client.bind((client_hostname, port))
# print("Binding Successful")
server_ip=input("Enter Server\'s IP Address:")
socket_client.connect((server_ip, port))

print("This is Client\'s IP Address: ", client_ip)

socket_client.close()
