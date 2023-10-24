
import socketio
import sys
import numpy as np
import cv2
from ffpyplayer.player import MediaPlayer
import json
import base64
from time import sleep


user=input("Your ID >")
path='video.mp4'
cap = cv2.VideoCapture('video.mp4')
sio = socketio.Client(reconnection=False)

@sio.event
def connect():
    print('connection established')

@sio.on('send_data')
def send_data():
    print("?????")
    try:
        sio.sleep(1)
        while True:
            ret,img=cap.read()
            #print(ret,img)
            if ret:
                #g1=cv2.imencode('.jpg', img)[1].tobytes()
                img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)
                
                #frame = cv2.imencode('.jpg', img)[1].tobytes()
                #print(len(img))
                #g1= base64.encodebytes(frame).decode("utf-8")
                #t1=len(g1)
                t1=len(img)
                #print(type(img))
                #print(len(img[0]))
                numbers=t1
                n1=0
                #print(numbers)
                #print(img[n1],img[n1].dtype)
                while (n1<numbers-1):
                    t2=""
                    for i in img[n1]:
                        for j in i:
                            t2=t2+str(j)+","
                    data={"num":n1,"content":t2}
                    sio.emit('receive',data)
                    n1=n1+1
                #message(frame)
                #t2=frame[n1*4096:]
                t2=""
                for i in img[n1]:
                    for j in i:
                        t2=t2+str(j)+","
                data={"numbers":numbers,"num":n1,"content":t2}
                sio.emit('receive_f',data)
                sleep(0)
            else:
                cap.release()
                sio.emit('disconnect1')
                break
    except KeyboardInterrupt:
        sys.exit()



@sio.on('message')
def message(data):
    sio.emit('receive',json)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://127.0.0.1:5000')
sio.wait()
