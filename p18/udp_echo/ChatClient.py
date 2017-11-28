# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data = raw_input('>')
    client_socket.sendto(data.encode(),('127.0.0.1',8000))
    if not data:
        break
    newdata = client_socket.recvfrom(1024)
    print('received from server:',repr(newdata))
client_socket.close()
