# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:49:19
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:50:31

'''
 Different module of setUp & tearDown hierarchy
'''

from __future__ import print_function

import unittest

class TestFoo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("foo setUpClass")
    @classmethod
    def tearDownClass(self):
        print("foo tearDownClass")
    def setUp(self):
        print("foo setUp")
    def tearDown(self):
        print("foo tearDown")
    def test_foo(self):
        self.assertTrue(True)

class TestBar(unittest.TestCase):
    def setUp(self):
        print("bar setUp")
    def tearDown(self):
        print("bar tearDown")
    def test_bar(self):
        self.assertTrue(True)
