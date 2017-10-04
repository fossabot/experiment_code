# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:53:55
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:55:15

from __future__ import print_function

import unittest

class TestArg(unittest.TestCase):
     def __init__(self, testname, arg):
        super(TestArg, self).__init__(testname)
        self._arg = arg
     def setUp(self):
         print("setUp:", self._arg)
     def test_arg(self):
         print("test_arg:", self._arg)
         self.assertTrue(True)

suite = unittest.TestSuite()
suite.addTest(TestArg('test_arg', 'foo'))
unittest.TextTestRunner(verbosity=2).run(suite)
