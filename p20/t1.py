# @author page
# @date 2017/11/27
# coding:utf-8
#!/usr/bin/python

import configparser

def init_create():
    config = configparser.ConfigParser()
    config['SystemInfo'] = {'port':8080}
    config['GameInfo'] = {'level':1,'score':100}
    with open('example.ini','w') as configfile:
        config.write(configfile)

def init_read_write():
    config = configparser.ConfigParser()
    config.read('example.ini')
    config['SystemInfo']['port'] = '9999'
    config.set('GameInfo','score','1000')
    for item in config.items('GameInfo'):
        print(item)
    with open('example.ini','w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    init_create()
    init_read_write()

