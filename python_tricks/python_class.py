# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-09 20:55:14
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-09 21:02:27

''' Problem : 你想改变对象实例的打印或显示输出，让它们更具可读性。

[解决方案]
要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法
'''

class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    # def __str__(self):
    #     return '({0.x!s},{0.y!s})'.format(self)

class DemoClass:
    '''This is a demonstation class 

    This text is the documents string that is 
    used to describe the class! 

    '''
    pass 

my_instance_1 = DemoClass()
print type(my_instance_1)
print id(my_instance_1)
print dir(DemoClass)
print dir(my_instance_1)
print DemoClass.__doc__
print DemoClass.__module__
if __name__ == '__main__':
    p = Pair(3,4)
    print 'p is {0!r}'.format(p)
    print p

