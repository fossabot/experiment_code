#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 21:37
# @Author  : Zhiwei Yang
# @File    : producer_consumer.py

import os
import time
from multiprocessing import Pool, Manager
import random


"""
本程序使用python3编写，可直接运行
程序中定义了两个类，分别是producer和consumer。每个类中的run方法，用于使用者填补实际功能代码。call方法为调度使用，请不要轻易修改。
在主函数中，初始化进程池以及manager对象，后者用于产生进程之间的队列、锁和Event。
主函数先创建多个producer进程，将producer进程们保存如列表producerProcessList，以便后面使用。
然后，主函数创建多个consumer进程，consumer进程从producer进程产生的数据队列中取出数据。
当所有producer进程运行完毕时，主函数设置结束event，通知各个consumer，当数据队列为空时，无需循环等待，直接结束进程即可。
进程池等待所有进程结束后，主函数运行完毕。
（不要问我为什么不用多线程。python的多线程，我只能说呵呵呵呵呵呵……）
下面是代码：


"""

# producer class
class producer(object):
    # do some action when object is init
    def __init__(self, initData):

        print("producer init...")
        self.initData = initData


        # producer manager

    def __call__(self, queueObj, lock, closeEvent):

        for result in self.run():
            with lock:
                queueObj.put(result)

                # function to be run, please write your code

    def run(self):

        for line in self.initData:
            print("producer %d put %s" % (os.getpid(), line.strip()))

            yield line.strip()


            # consumer class


class consumer(object):
    # do some action when object is init
    def __init__(self):

        print("consumer init...")

        # consumer manager

    def __call__(self, queueObj, lock, closeEvent):

        while 1:

            with lock:
                if queueObj.empty():

                    if closeEvent.is_set() is True:

                        break
                    else:
                        time.sleep(0.01)
                        continue

                data = queueObj.get()
            self.run(data)

            # function to be run, please write your code

    def run(self, data):

        print("consumer %d get %s" % (os.getpid(), data))


if __name__ == '__main__':

    print("mission start, main process is %d" % os.getpid())

    pool = Pool(6)
    q = Manager().Queue()
    lock = Manager().Lock()
    event = Manager().Event()

    # 用于控制所有producer工作完毕后，设置结束Event
    producerProcessList = []

    for i in range(1, 4):
        lines = ["%d" % random.randint(10, 20)] * random.randint(10, 20)
        obj = producer(lines)
        producerProcessList.append(
            pool.apply_async(obj, (q, lock, event))
        )

    for i in range(2):
        obj = consumer()
        pool.apply_async(obj, (q, lock, event))

    pool.close()

    for ps in producerProcessList:
        ps.get()
        print("one of the producer finished")

    print("all producer are finished, so event is set")
    event.set()

    pool.join()

    print("mission finished, main process is %d" % os.getpid())