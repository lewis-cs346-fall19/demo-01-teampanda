# Programmer: Aniket Panda
# CSC 346 Lab 1 client

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 12121)
sock.connect(addr)
for i in range(10):
    # print("in client loop")
    try:
        # print("entered client try")
        sock.sendall(str(i).encode())
        msg = sock.recv(1024).decode()
        print(msg)
    except:
        socket.close()
