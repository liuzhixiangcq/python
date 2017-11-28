# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.sendto(b'hello',('127.0.0.1',8000))
newdata,addr = client_socket.recvfrom(1024)
print('sentence:',newdata.decode())
client_socket.close()
