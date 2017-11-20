#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 21:37
# @Author  : Zhiwei Yang
# @File    : producer_consumer.py
# /usr/bin/env python3
# encoding = utf-8
import os
import time
from multiprocessing import Pool, Manager
import random


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