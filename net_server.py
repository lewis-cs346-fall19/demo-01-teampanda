# Programmer: Aniket Panda
# CSC 346 Lab 1 server

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 12121)
sock.bind(addr)
sock.listen(5)
(connectedSock, clientAddress) = sock.accept()
while (True):
    #print("in server loop")
    try:
        #print("entered server try")
        msg = connectedSock.recv(1024).decode()
        msg = int(msg)*2
        msg = str(msg)
        connectedSock.sendall(msg.encode())
    except:
        connectedSock.close()
        sock.close()
        
    
