# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',8000))
server_socket.listen(5)
client_socket , client_addr = server_socket.accept()
print('connection from ',client_addr)
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print('received from client:',repr(data))
    print('Echo:',repr(data))
    client_socket.send(data)
client_socket.close()
server_socket.close()
