# @author page
# @date 2017/11/27
# coding:utf-8
#!/usr/bin/python

import threading
import time
import random

def timer(intval):
    for i in range(5):
        time.sleep(random.choice(range(intval)))
        thread_id = threading._get_ident()
        print('Thread:{0} Time:{1} \n'.format(thread_id,time.ctime()))

def test():
    t1 = threading.Thread(target = timer,args = (5,))
    t2 = threading.Thread(target = timer,args = (5,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    test()
