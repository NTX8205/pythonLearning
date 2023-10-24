import socketio

sio = socketio.Client(reconnection=False)

@sio.event
def connect():
    print('connection established')

@sio.on('message')
def message(data):
    print('message received from server:', data)
    sio.sleep(1)
    if sio.connected:
        sio.send("hi and bye bye")
    sio.sleep(1)
    if sio.connected:
        sio.emit('disconnect')

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://10.0.52.235:5000')
sio.wait()