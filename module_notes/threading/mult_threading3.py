# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-19 14:00:18
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-19 14:20:11

import time
import threading

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
threads.append(thread1)
thread2 = myThread(2, "Thread-2", 2)
threads.append(thread2)

thread1.setDaemon(True)
thread2.setDaemon(True)

# 开启新线程
thread1.start()
thread2.start()

print ("退出主线程")