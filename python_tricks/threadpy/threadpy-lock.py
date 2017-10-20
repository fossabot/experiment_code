# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-19 15:25:33
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-19 15:32:11
from threading import Thread,Lock
import time
_base = 1
_lock = Lock()
"""
根据上面代码执行的结果可以发现，compute_sum/t.run 函数的执行是按照 start() 的顺序，但 _sum 结果的输出顺序却是随机的。因为  _sum 中加入了 time.sleep(2.0) ，让程序执行到这里就会进入阻塞状态，但是几个线程的执行看起来却像是同时进行的（并发）。

有时候我们既需要并发地“跳过“阻塞的部分，又需要有序地执行其它部分，例如操作共享数据的时候，这时就需要用到”锁“。在上述”求和线程“的例子中，假设每次求和都需要加上额外的 _base 并把计算结果累积到 _base 中。尽管这个例子不太恰当，但它说明了线程锁的用途

"""

class ComputeSum(Thread):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y

    def run(self):
        result = self._sum(self.x,self.y)
        print("{} + {} + base = {}".format(self.x, self.y, result))

    def _sum(self,x,y):
        print("Compute {} + {}...".format(x, y))
        time.sleep(2.0)
        global _base
        with _lock:
            result = x + y + _base
            _base = result
        return result

threads = [ComputeSum(0,0),ComputeSum(1,1),ComputeSum(2,2)]
start = time.time()

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Total elapsed time {} s".format(time.time() - start))


