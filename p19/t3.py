# @author page
# @date 2017/11/27
# coding:utf-8
#!/usr/bin/python

import threading
import time
import random

class MyThread(threading.Thread):
    
    def __init__(self,intval):
        threading.Thread.__init__(self)
        self.intval = intval
    
    def run(self):
        for i in range(5):
            time.sleep(random.choice(range(self.intval)))
            thread_id = threading._get_ident()
            print('Thread:{0} Time:{1}\n'.format(thread_id,time.ctime()))

def test():
    t1 = MyThread(8)
    t1.name = 't1'
    t1.start()
    print('main thread waiting 2s')
    t1.join(2)
    print('main thread wait end')
    t1.join()
    print('wait ended')

if __name__ == '__main__':
    
    test()

