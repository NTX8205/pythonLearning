# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 06:45:05 2021

@author: User
"""

import eventlet
import socketio
import os

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

client={}
def write_bin(file2,data1):
    try:
        f1=open(file2,"wb")
        f1.write(data1)
        print("done")
        f1.close()
    except IOError as e:
        print("Error while handling files", e)

@sio.on('combine')
def combine(sid, data):
    filename=data['fname']
    base=data['base']
    count=data['count']            
    try:
        f1=open(filename,"ab")
        c=0
        while c<count:
            f2=open(base+"-"+str(c)+".sep","rb")
            bytes_read = f2.read(4096)
            f1.write(bytes_read)
            f2.close()
            os.remove(base+"-"+str(c)+".sep")
            c=c+1
        f1.close()
        sio.sleep(2)
        sio.emit("disconnect")
        disconnect1(sid)
    except IOError as e:
        print("Error while handling files", e)


@sio.event
def connect(sid, environ):
    print('connect ', sid)
    print('send hello to client')
    #sio.send("hello")
    sio.emit("send")

@sio.on('receive')
def receive(sid, data):
    file2=data['name']
    print(file2)
    write_bin(file2,data['data_bytes'])
    print("?????")

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
