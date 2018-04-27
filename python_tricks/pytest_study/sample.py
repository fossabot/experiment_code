# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-27 10:14:12
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-27 10:27:30

import pytest


def test_answer1():
    assert  1 + 2 == 3

class TestSample1:
   def test_answer2(self):
       print('this is a log')
       assert 1 + 2 == 3


"""
说到测试框架自然要说到setup和teardown两个方法.

setup是用来做准备操作.一般用来初始化资源.
teardown是用来做收尾操作.一般用了关闭资源.
pytest的setup和teardown是利用@pytest.fixture这个注释来完成的.不仅可以完成初始化操作,初始化后如果有数据需要给用例使用也是非常方便!
"""

class TestSample2:
   # @pytest.fixture()
   # def count(self):
   #     print('init count')
   #     return 10
   def test_answer3(self, count,count2):
       print('get count %s' % count)
       print('get count %s' % count2)
       assert count == 10
   def test_answer_4(self, count,count2):
       print('test_answer_2 get count %s' % count)
       print('get count %s' % count2)
       assert count == 10

