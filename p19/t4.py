# @author page
# @date 2017/11/27
# coding:utf-8
#!/usr/bin/python

import threading
import time
import random

class Account(threading.Thread):

    lock = threading.Lock()
    def __init__(self,account):
        threading.Thread.__init__(self)
        Account.account = account

    def run(self):
        self.get_money()

    def get_money(self):
        Account.lock.acquire()
        t = threading.current_thread()
        m = random.choice(range(50,100))
        if Account.account < m:
            print('{0} failed left:{1} to get:{2}'.format(t.name,Account.account,m))
            Account.lock.release()
            return 0
        time.sleep(random.choice(range(5)))
        pre = Account.account
        Account.account -= m
        print('{0} ok left:{1} get:{2} left:{3}'.format(t.name,pre,m,Account.account))
        Account.lock.release()

def test():
    for i in range(5):
        Account(200).start()

if __name__ == '__main__':
    test()

