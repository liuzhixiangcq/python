# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',8000))
while True:
    data = raw_input()
    client_socket.send(data.encode())
    if not data:
        break
    newdata = client_socket.recv(1024)
    print('received from server:',repr(newdata))
client_socket.close()
