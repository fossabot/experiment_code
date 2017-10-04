# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:52:05
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:53:37

import unittest

class TestRaiseException(unittest.TestCase):
    def test_raise_except(self):
        with self.assertRaises(SystemError):
            raise SystemError

suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(TestRaiseException)
unittest.TextTestRunner().run(suite)

class TestRaiseFail(unittest.TestCase):
    def test_raise_fail(self):
        with self.assertRaises(SystemError):
            pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestRaiseFail)
unittest.TextTestRunner(verbosity=2).run(suite)
