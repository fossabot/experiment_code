# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 16:01:44
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 16:20:49

from __future__ import print_function
import unittest

# test success under py3.6.1
class TestSkip(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def tearDown(self):
        print("tearDown")
    @unittest.skip("skip this test")
    def test_skip(self):
        raise RuntimeError
    def test_not_skip(self):
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSkip)
unittest.TextTestRunner(verbosity=2).run(suite)
