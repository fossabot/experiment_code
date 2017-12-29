#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 10:47
# @Author  : Zhiwei Yang
# @File    : class_static.py.py
class example(object):
  @classmethod
  def clsmethod(cls):
    print ("I am classmethod")
  @staticmethod
  def stmethod():
    print ("I am staticmethod")
  def instmethod(self):
    print ("I am instancemethod")

ex = example()
ex.clsmethod()
# I am classmethod
ex.stmethod()
# I am staticmethod
ex.instmethod()
# I am instancemethod
example.clsmethod()
# I am classmethod
example.stmethod()
# I am staticmethod
example.instmethod()
# Traceback (most recent call last):
#   File "", line 1, in
# TypeError: unbound method instmethod() ...