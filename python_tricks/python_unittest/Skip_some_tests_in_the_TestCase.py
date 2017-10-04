# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:58:23
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:58:46

import unittest
RUN_FOO = False
DONT_RUN_BAR = False
class TestSkip(unittest.TestCase):
    def test_always_run(self):
        self.assertTrue(True)
    @unittest.skip("always skip this test")
    def test_always_skip(self):
        raise RuntimeError
    @unittest.skipIf(RUN_FOO == False, "demo skipIf")
    def test_skipif(self):
        raise RuntimeError
    @unittest.skipUnless(DONT_RUN_BAR == True, "demo skipUnless")
    def test_skipunless(self):
        raise RuntimeError

suite = unittest.TestLoader().loadTestsFromTestCase(TestSkip)
unittest.TextTestRunner(verbosity=2).run(suite)
