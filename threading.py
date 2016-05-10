# -*- coding:utf-8 -*-

import time, threading

# 创建一个threading.Thread对象，在它的初始化函数（__init__）中将可调用对象作为参数传入
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name



'''
Result:
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
'''

'''
t.setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
'''

# 通过继承Thread类，重写它的run方法
import threading, time, random
count = 0
class Counter(threading.Thread):
    def __init__(self, lock, threadName):
        '''
        lock: 琐对象
        threadName: 线程名称
        '''
        super(Counter, self).__init__(name=threadName)  #注意：一定要显式的调用父类的初始化函数。
        self.lock = lock
    
    def run(self):
        '''
        重写父类run方法，在线程启动后执行该方法内的代码。
        '''
        global count
        self.lock.acquire()
        for i in xrange(10000):
            count = count + 1
        self.lock.release()

lock = threading.Lock()
for i in range(5): 
    Counter(lock, "thread-" + str(i)).start()
time.sleep(2)   #确保线程都执行完毕
print count
