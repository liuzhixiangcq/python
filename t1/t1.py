# @author page
# @date 2017/11/23

# coding:utf-8
# !/usr/bin/python

from Tkinter import *

def sayHello():
    print 'hello,gui!'

root = Tk()
root.title('window')
root.geometry()
com = Button(root,text = 'click',command = sayHello)
com.pack(side = BOTTOM)
root.mainloop()
