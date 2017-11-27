# @author page
# @date 2017/11/27
# coding:utf-8
#!/usr/bin/python

import threading
import time
import random

class ConContainer():

    def __init__(self,flag):
        self.contents = 0
        self.avalable = False
        self.cv = threading.Condition()
        self.cond = flag

    def produce(self,value):

        if self.cond:
            with self.cv:
                if self.avalable:
                    self.cv.wait()
                self.contents = value
                t = threading.current_thread()
                print('{0} produce {1}'.format(t.name,self.contents))
                self.avalable = True
                self.cv.notify()
        else:
            if self.avalable:
                pass
            else:
                self.contents = value
                t = threading.current_thread()
                print('{0} produce {1}'.format(t.name,self.contents))
                self.avalable = True
    
    def consume(self):

        if self.cond:
            with self.cv:
                if not self.avalable:
                    self.cv.wait()
                t = threading.current_thread()
                print('{0} consume {1}'.format(t.name,self.contents))
                self.avalable = False
                self.cv.notify()
        else:
            if not self.avalable:
                pass
            else:
                t = threading.current_thread()
                print('{0} consume {1}'.format(t.name,self.contents))
                self.avalable = False

class Producer(threading.Thread):

    def __init__(self,container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        for i in range(1,10):
            time.sleep(random.choice(range(5)))
            self.container.produce(i)

class Consumer(threading.Thread):

    def __init__(self,container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        for i in range(1,10):
            time.sleep(random.choice(range(5)))
            self.container.consume()

def test1():
    
    container = ConContainer(True)
    Producer(container).start()
    Consumer(container).start()

def test():
    container = ConContainer(False)
    Producer(container).start()
    Consumer(container).start()

if __name__ == '__main__':

    test()

    print('sleep')
    time.sleep(30)
    print('sleep end')
    test1()





