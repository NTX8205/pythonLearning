# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:46:01 2021

@author: User
"""



#importing libraries
import socket
import cv2
import pickle
import struct
import imutils

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
#host_ip = socket.gethostbyname(host_name)
host_ip = '127.0.0.1'
print('HOST IP:',host_ip)
port = 10050
socket_address = (host_ip,port)
print('Socket created')
# bind the socket to the host. 
#The values passed to bind() depend on the address family of the socket
server_socket.bind(socket_address)
print('Socket bind complete')
server_socket.listen(5)
flag=False
print('Socket now listening')
while not flag:
    client_socket,addr = server_socket.accept()
    print('Connection from:',addr)
    if client_socket:
        vid = cv2.VideoCapture('video.mp4')
        while(vid.isOpened()):
            img,frame = vid.read()
            if not img:
                client_socket.close()
                vid.release()
                cv2.destroyAllWindows()
                flag=True
                break
            else:
                a = pickle.dumps(frame)
                message = struct.pack("Q",len(a))+a
                client_socket.sendall(message)
                cv2.imshow('Sending...',frame)
                key = cv2.waitKey(10) 
                if key ==13:
                    client_socket.close()
                    vid.release()
                    cv2.destroyAllWindows()
                    flag=True
                    break
server_socket.close()