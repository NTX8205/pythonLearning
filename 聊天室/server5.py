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
    write_bin("temp1_"+str(data['num'])+".sep",data['content'])
    

@sio.on('receive_f')
def receive_f(sid, data):
    write_bin("temp1_"+str(data['num'])+".sep",data['content'])
    #print("done")
    count=data['numbers']
    #print(count)
    t1=[]
    try:
        c=0
        while c<count:
            f2=open("temp1_"+str(c)+".sep","r")
            data1 = f2.read()
            temp=data1.split(",")
            i=0
            b=[]
            while (i+3<len(temp)):
                temp1=[np.uint8(int(temp[i])), np.uint8(int(temp[i+1])),np.uint8(int(temp[i+2]))]
                b.insert(len(b),temp1)
                i=i+3
            t1.insert(len(t1),b)
            f2.close()
            os.remove("temp1_"+str(c)+".sep")
            c=c+1
        #print(len(t1))
        #show(t1)
        t2=np.array(t1)
        #print(t2.dtype)
        #t3=base64.decodebytes(t2)
        #t3=np.array(t3)
        #img_decode = cv2.imdecode(t2, cv2.IMREAD_COLOR)
        #print("h1!")
        cv2.imshow("img_decode", t2)
        if cv2.waitKey(1)==10:
            cv2.destroyAllWindows()
            sio.sleep(1)
        #sio.emit("disconnect")
        #disconnect1(sid)
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