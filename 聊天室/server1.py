import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    print('send hello to client')
    sio.send("hello")
   
@sio.on('message')
def message(sid, data):
    print('message got from client:', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    sio.emit('disconnect')

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)