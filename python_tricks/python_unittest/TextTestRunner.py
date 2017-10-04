# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:51:09
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:51:46

import unittest

class TestFoo(unittest.TestCase):
    def test_foo(self):
         self.assertTrue(True)
    def test_bar(self):
         self.assertFalse(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
unittest.TextTestRunner(verbosity=2).run(suite)
