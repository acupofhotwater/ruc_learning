# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import threading
import pygame
import time
import os 

""" game setting"""
# screen

# create enemy event
ENEMY_EVENT_PERIOD = "1000"
# fire
HERO_FIRE_EVENT_PERIOD = "500"

game_setting = [ENEMY_EVENT_PERIOD, HERO_FIRE_EVENT_PERIOD]

""" tcplink """
def tcplink(client_conn, addr, game_setting):
    print ("the new client is ", addr)

    while True:
        # start game
        print ("wait new msg")
        raw_msg = client_conn.recv(1024)
        if not raw_msg:
            break
        msg = raw_msg.decode("UTF-8").split()[0]
        print ("msg of client",msg)

        # send init game_setting ; pictures to do
        if msg == "start":
            print ("start to send msg")
            for data in game_setting:
                time.sleep(0.2)
                client_conn.send(data.encode("UTF-8"))
            print ("send game setting")
        # get clietn score todo 

        # game over todo
        
    print("disconnect the client of ",addr)
    client_conn.close()

"""comunicate with socket"""
plane_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set host port
host = socket.gethostname()
port = 9999
# socket bind port
plane_socket.bind((host, port))
plane_socket.listen(5)

while True:
    # create client connect
    client_conn, addr = plane_socket.accept()
    # create new thread to deal with tcp link
    t = threading.Thread(target= tcplink, args = (client_conn, addr, game_setting))
    t.start()
