
import os
import socket 

#1. making the socket 
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = '192.168.0.6'
port = 1234

#2. binding the socket
server.bind((ip , port))
print(f"\n The server socket is created at ip {ip} and port {port}")

#3. ready to listening
server.listen()
print('\nserver is ready to listen to client')

#4. accept the client
client_socket , client_addr = server.accept()

msg = f"Welcome at ip : {client_addr[0]} and port : {client_addr[1]}"

#5. sending 
client_socket.send(msg.encode())

#6. receving
print('\nwaiting for msg form client.......')

cmsg = client_socket.recv(1024).decode()

print('\nclient msg: ',cmsg)
   
