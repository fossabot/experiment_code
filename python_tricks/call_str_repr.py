#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 17:13
# @Author  : Zhiwei Yang
# @File    : call_str_repr.py.py

class print_name(object):
    def __init__(self,name):
        self.name = name

class print_name_pro(object):

    def __int__(self,name):
        self.name = name
    def __str__(self):
        return "%s" % self.name

if __name__ == '__main__':
    a = print_name("yang")
    print (a) # 这样打印不好看，所以请看类B

    b = print_name_pro("zhi")
    print (b)