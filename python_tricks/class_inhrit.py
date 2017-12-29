#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 22:29
# @Author  : Zhiwei Yang
# @File    : class_inhrit.py.py

class A(object):
    def show(self):
        print("base show")

class B(A):
    def show(self):
        print("de show")

class C(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print("a=",self.__a,"b=",self.__b)

    def __call__(self, num):
        print ("call:",num + self.__a)

class D(object):
    # 方法__getattr__只有当没有定义的方法调用时，才是调用他。当fn1方法传入参数时，
    # 我们可以给mydefault方法增加一个*args不定参数来兼容。
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("init")

    def mydefault(self,*args):
        print("default!" + str(args[0]))

    def __getattr__(self, name):
        print ("function: ",name)
        return self.mydefault

if __name__ == '__main__':
    b = B()
    b.show()
    a = A()
    a.show()
    c = C(10,20)
    c.myprint()
    c(100)
    print("*"* 40)
    d = D(100,200)
    d.f1(1)
    d.f2("hello")
    d.f3(10)