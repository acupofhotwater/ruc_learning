# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket
import threading
import os

# tcplink
def tcplink(conn, addr):
    print('the new connect is',addr)

    while True:
        print('等待新指令')
        data = conn.recv(1024)
        if not data:
            print('disconenct with client ')
            break
        cmd,c_filename = data.decode().split()
        print('文件名是：',c_filename)
        filename = os.path.join("/home/acupofwater/Desktop", c_filename)
        print (filename)
        print (os.path.isfile(filename))
        if os.path.isfile(filename):
            # send file size to client
            file_size = os.path.getsize(filename)
            print(file_size)
            conn.send(str(file_size).encode("UTF-8"))
            print("send file_size ") #ok

            # recv client ack
            client_ack = conn.recv(1024)
            print('来自客户端的确认信息：',client_ack.decode("UTF-8"))
            
            # send file
            f = open(filename,'rb')
            for line in f:
                conn.send(line)
            f.close()
            print('send done')

    conn.close()

# create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set host port
host = socket.gethostname()
port = 12345
# bind port 
server.bind((host,port))
server.listen(5)

while True:
    #create client connect
    conn,addr = server.accept()

    # TCP:
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()
