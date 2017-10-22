# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-20 09:40:13
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-20 09:57:30

class Wait(object):
    """
    由于 Coroutine 协议规定 await 后只能跟 awaitable 对象，
    而 awaitable 对象必须是实现了 __await__ 方法且返回迭代器
    或者也是一个协程对象，
    因此这里临时实现一个 awaitable 对象。
    """

    def __init__(self,index):
        self.index = index
    def __await__(self):
        return (yield self.index)

async def jump_range(upper):
    index = 0
    while index < upper:
        jump = await Wait(index)
        if jump is None:
            jump = 1
        index += jump

jump = jump_range(5)
print(jump)
print(jump.send(None))
print(jump.send(3))
print(jump.send(None))
