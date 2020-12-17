
import os
import socket

#1. making of socket
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#2. connecting to sever
ip = input("\nEnter the sever's ip: ")
port = int(input("\nEnter the sever's port no. "))

print('\nTrying to conect.......')
client.connect((ip,port))

print('\nSuccessfully CONNECTED')

#3.receving the msg
print('\nWaiting for the message......')

smsg = client.recv(1024).decode()
print("\nServer msg: ",smsg)

msg = "Thanks a lot...."

client.send(msg.encode())
print("\n Closing the socket....")

client.close()
