
import os 
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.0.6'
port = 1234

server.bind((ip,port))
print(f'\nSrever Socket craeted at IP:{ip} and Port:{port}')

print('\n\nServer TRYING TO CONNECT.....')
server.listen()

c_soc,c_addr = server.accept()
msg = '\nConnected Successfully'

print(msg)

c_soc.send(msg.encode())
c_soc.send(f"\n\nWelcome to the Client Socket at IP: {c_addr[0]} and Port: {c_addr[1]}".encode())


l = ['bye' ,'buhbye', 'by', 'tata', 'see you' ,'ttly', 'gtg']


while True:
    
    msg = input('Sever: ')
    c_soc.send(msg.encode())
    
    if msg.lower().strip() in l:
        print("\nServer side wants to close the side")
        server.close()
        c_soc.close()
        break
    
    cmsg = c_soc.recv(1024).decode()
    print('\nClient: ',cmsg) 
    if cmsg.lower().strip() in l:
        
        print('\nClient side wants to close the side')
        server.close()
        c_soc.close()
        break
