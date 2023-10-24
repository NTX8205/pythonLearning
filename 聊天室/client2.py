# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 06:46:11 2021

@author: User
"""

import socketio
user=input("Your ID >")
sio = socketio.Client(reconnection=False)

@sio.event
def connect():
    print('connection established')

@sio.event
def talk():
    print(">",end="")
    t=input()
    data={'message':t,'user':user}
    sio.sleep(1)
    if sio.connected:
        sio.send(data)


@sio.on('message')
def message(data):
    if data.find("quit")>-1:
        sio.sleep(1)
        if sio.connected:
            sio.emit("disconnect")
    else:
        print(data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.110.116:5000')
sio.wait()
