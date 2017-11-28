# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python 

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1',8000))

while True:
    data , addr = server_socket.recvfrom(1024)
    if not data:
        break
    print('received from client:',addr,repr(data))
    server_socket.sendto(data,addr)
server_socket.close()
