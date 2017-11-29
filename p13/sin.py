# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python

from Tkinter import *
import math
def Sin():
    width = 510
    height = 210
    orign_x = 2
    orign_y = height / 2
    scale_x = 40
    scale_y = 100
    end_arc = 360 * 2
    ox = 0
    oy = 0
    x = 0
    y = 0
    arc = 0 
    root = Tk()
    c = Canvas(root,bg = 'white', width = 510 , height = 210)
    c.pack()
    c.create_text(200,20,text = ' y = sin(x)')
    c.create_line(0,orign_y,width,orign_y)
    for i in range(0,end_arc + 1,10):
        arc = math.pi * i * 2 / 360
        #x = scale_x * arc
        #y = scale_y * math.sin(arc)
        x = orign_x + arc * scale_x
        y = orign_y - math.sin(arc) * scale_y
        c.create_line(ox,oy,x,y)
        ox = x
        oy = y
    root.mainloop()

if __name__ == '__main__':
    Sin()
    print('call Sin() end')
