# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-19 15:04:49
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-19 15:18:36

from threading import Thread
import time

def _sum(x,y):
    print("compute {} + {}...".format(x,y))
    time.sleep(2.0)
    return x + y

def compute_sum(x,y):
    result = _sum(x,y)
    print("{} + {} + {}".format(x,y,result))

start = time.time()
# 将函数传递给 Thread 创建线程实例之外
threads = [
    Thread(target=compute_sum,args=(0,0)),
    Thread(target=compute_sum,args=(1,1)),
    Thread(target=compute_sum,args=(2,2)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Total elapsed time {} s".format(time.time()-start))

start = time.time()
compute_sum(0,0)
compute_sum(1,1)
compute_sum(2,2)
print("Total elapsed time {} s".format(time.time()-start))
