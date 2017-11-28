# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python

import socket
import random

quotas = ['hello','good morning','good evening','how are you?']

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1',8000))

while True:
    data , addr = server_socket.recvfrom(1024)
    quota = random.choice(quotas)
    server_socket.sendto(quota.encode(),addr)
server_socket.close()

