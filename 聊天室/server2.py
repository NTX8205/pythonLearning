# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 06:45:05 2021

@author: User
"""

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

client=[]
@sio.event
def connect(sid, environ):
    print('connect ', sid)
    print('send hello to client')
    sio.enter_room(sid,"/chat")
    client.append(str(sid))
    sio.send("hello")
    sio.emit("talk")


@sio.on('message')
def message(sid, data):
    if data['message'].find("/quit")>-1:
        t='User '+data['user']+" will leave!"
        sio.emit('disconnect',to=sid)
        disconnect1(sid)
        sio.send(t,skip_sid=sid)
        sio.emit("talk",skip_sid = sid)
    else:
        t=data['user']+" : "+ data['message']
        sio.send(t)
        sio.emit("talk")

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
    eventlet.wsgi.server(eventlet.listen(('192.168.110.116', 5000)), app)
