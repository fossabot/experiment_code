# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 16:10:33
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 16:11:41

from __future__ import print_function
import unittest

def old_func_test():
    assert "Hello" == "Hello"

def old_func_setup():
    print("setup")

def old_func_teardown():
    print("teardown")

testcase = unittest.FunctionTestCase(old_func_test,setUp=old_func_setup,
    tearDown=old_func_teardown)
suite = unittest.TestSuite([testcase])
unittest.TextTestRunner().run(suite)
