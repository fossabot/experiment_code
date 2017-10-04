# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:57:15
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:57:41

import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        assert "foo" == "foo"

class TestBar(unittest.TestCase):
    def test_bar(self):
        assert "bar" == "bar"

suite = unittest.TestSuite()
suite.addTest(TestFoo('test_foo'))
suite.addTest(TestBar('test_bar'))
unittest.TextTestRunner(verbosity=2).run(suite)
