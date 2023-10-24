import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

client={}
@sio.event
def connect(sid, environ):
    print('connect ', sid)
    print('send hello to client')
    sio.enter_room(sid,"/")
    client[str(sid)]={'id':str(sid), 'room':'/'}
    sio.emit("join")

@sio.event
def join(sid, room):
    sio.enter_room(sid,room)
    print("User",sid," now is at room",room)
    client[str(sid)]['room']=room
    t="welcome to the room "+room
    sio.send(t,room)
    sio.emit("talk")

@sio.on('message')
def message(sid, data):
    if data['message'].find("/quit")>-1:
        t='User '+data['user']+" will leave!"
        sio.emit('disconnect',to=sid)
        room1=client[str(sid)]['room']
        disconnect1(sid)
        sio.send(t,skip_sid=sid,room=room1)
        sio.emit("talk",skip_sid = sid,room=room1)
    else:
        t=data['user']+" : "+ data['message']
        room1=client[str(sid)]['room']
        sio.send(t,room=room1)
        print(t,"====",room1)
        sio.emit("talk",room=room1)

@sio.event
def disconnect1(sid):
    print('disconnect ', sid)
    sio.leave_room(sid,room=client[str(sid)]['room'])
    sio.emit('disconnect',to=sid)
    del client[str(sid)]
    sio.disconnect(sid)
    sio.sleep(1)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('192.168.110.116', 5000)), app)
