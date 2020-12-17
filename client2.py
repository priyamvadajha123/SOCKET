
import os 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "192.168.0.6"
port = 1234

client.connect((ip,port))

smsg = client.recv(1024).decode()
print(smsg)
smsg = client.recv(1024).decode()
print(smsg)

l = ['bye' ,'buhbye', 'by', 'tata', 'see you' ,'ttly', 'gtg']
flag = True
while flag:
    smsg = client.recv(1024).decode()
    print('\nSever: ',smsg)
    
    for i in smsg.lower().strip().split():
        if i in l:
            print('\nSever side wants to close the chat')
            flag = False
            client.close()
            break
    else:
        cmsg = input('Client: ')
        client.send(cmsg.encode())

        for i in cmsg.lower().strip().split(): 
            if i in l:
                print('\nClient side wants to close the chat')
                flag = False
                client.close()
                break
