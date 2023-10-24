
import socketio
import sys
user=input("Your ID >")
sio = socketio.Client(reconnection=False)
def reading(file1):
    t3=[]
    print("pass1-1")
    print(file1)
    try:
       # print(file1)
        with open(file1, "rb") as f:
           byte = f.read(1)
           while byte != b"":
               # Do stuff with byte.
               t3.append(byte)
               byte = f.read(1)
    except IOError as e:
        print("Error while handling files", e)
    return t3
@sio.event
def connect():
    print('connection established')

@sio.on('send')
def send():
    file1="python_advance.pptx"
    base=file1[:file1.find(".")]
    end=file1[file1.find(".")+1:]
    try:
        
       # print(file1)
        with open(file1, "rb") as f:
            count=0
            sio.sleep(1)
            while True:
                bytes_read = f.read(4096)
                if not bytes_read:
                    # file transmitting is done
                    break
                data={"name":base+"-"+str(count)+".sep",'data_bytes': bytes_read}
                
                sio.call("receive",data)
                count=count+1
        data={"fname":base+"_2."+end,"base":base,"count":count}
        print("combine")
        sio.sleep(2)
        sio.call("combine",data)
        sio.sleep(2)
    except KeyboardInterrupt:
        sys.exit()

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

sio.connect('http://127.0.0.1:5000')
sio.wait()
