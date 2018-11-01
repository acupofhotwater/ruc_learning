#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket

# create client socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host port
host = socket.gethostname()
port = 12345
# connect server
client.connect((host, port))

while True:
    #input filename for download
    cmd = input('>>>').strip()
    if not cmd:
        break
    if cmd.startswith('get'):
        # send file name 
        client.send(cmd.encode("UTF-8"))
        print("send file name")

        # recv file size 
        file_total_size = int(client.recv(1024))
        print('file size',file_total_size)

        # ready to recv file
        client.send('client is ready'.encode("UTF-8"))
        print("start recv file")
        received_size = 0
        filename = "/home/zh/Documents/ados/test/ftp_test/" + "new" + cmd.split(" ")[1]
        f = open(filename,'wb')
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            print('received size:',received_size)
            f.write(data)
        else:
            print('received size',received_size)
            f.close()
        print ("download ok\n")

client.close()