# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:46:10
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:47:59

from __future__ import print_function
import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertTrue(True)

    def fun_not_run(self):
        print("not run")

    def test_foo(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
