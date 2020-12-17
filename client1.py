
import os 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input('\nEnter the IP: ')
port = int(input('\nEnter the Port: '))

client.connect((ip,port))

smsg = client.recv(1024).decode()
print(smsg)
smsg = client.recv(1024).decode()
print(smsg)

l = ['bye' ,'buhbye', 'by', 'tata', 'see you' ,'ttly', 'gtg']

while  True:
    smsg = client.recv(1024).decode()
    print('\nSever: ',smsg)
    
    if smsg.lower().strip() in l:
        print('\nSever side wants to close the chat')
        client.close()
        break

    cmsg = input('Client: ')
    client.send(cmsg.encode())
    
    if cmsg.lower().strip() in l:
        print('\nClient side wants to close the chat')
        client.close()
        break
    
