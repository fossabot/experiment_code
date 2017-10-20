# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-19 15:18:57
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-19 15:23:18

from threading import Thread
import time

class ComputeSum(Thread):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
    def run(self):
        result = self._sum(self.x,self.y)
        print("{} + {} = {}".format(self.x, self.y, result))

    def _sum(self,x,y):
        print("{} + {}".format(self.x, self.y))
        time.sleep(2.0)
        return x + y

theads = [ComputeSum(0,0),ComputeSum(1,1),ComputeSum(2,2)]
start = time.time()

for t in theads:
    t.start()
for t in theads:
    t.join()

print("Total elapsed time {} s".format(time.time() - start))
