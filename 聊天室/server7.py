# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:59:06 2021

@author: jains
"""


import eventlet
import socketio
import os
import numpy as np
import cv2
import base64
from ffpyplayer.player import MediaPlayer

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

client={}

frames1=""

def write_bin(file2,data1):
    try:
        f1=open(file2,"w")
        f1.write(data1)
        #print("done")
        f1.close()
    except IOError as e:
        print("Error while handling files", e)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    print('send hello to client')
    #sio.send("hello")
    pingpong(sid)

@sio.event()
def pingpong(sid):
    print("/////")
    sio.emit("send_data")

@sio.on('receive')
def receive(sid, data):
    #print(data)
    #file2=data['name']
    #print(file2)
    global frames1
    frames1=frames1+data['content']+"\n"
    #write_bin("temp1_"+str(data['num'])+".sep",data['content'])
    

@sio.on('receive_f')
def receive_f(sid, data):
    write_bin("temp1_"+str(data['num'])+".sep",data['content'])
    global frames1
    frames1=frames1+data['content']
    #print("done")
    #print(count)
    try:
        t1=[]
        temp1=frames1.split("\n")
        for k in temp1:
            temp=k.split(",")
            i=0
            b=[]
            while (i+3<len(temp)):
                temp1=[np.uint8(int(temp[i])), np.uint8(int(temp[i+1])),np.uint8(int(temp[i+2]))]
                b.insert(len(b),temp1)
                i=i+3
            t1.insert(len(t1),b)
        t2=np.array(t1)
        cv2.imshow("img_decode", t2)
        if cv2.waitKey(1)==10:
            cv2.destroyAllWindows()
            sio.sleep(1)
        #sio.emit("disconnect")
        #disconnect1(sid)
        frames1=""
    except IOError as e:
        print("Error while handling files", e)
    
    
@sio.event
def disconnect1(sid):
    
    print('disconnect ', sid)
    sio.leave_room(sid,"/chat")
    sio.emit('disconnect',to=sid)
    for i in client:
        if i==str(sid):
            client.remove(i)
            break
    sio.disconnect(sid)
    sio.sleep(1)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)