# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:56:00
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:56:47

import unittest
class TestFooBar(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(True)
    def test_bar(self):
        self.assertTrue(True)

class TestHelloWorld(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("Hello", "Hello")
    def test_world(self):
        self.assertEqual("World", "World")

suite_loader = unittest.TestLoader()
suite1 = suite_loader.loadTestsFromTestCase(TestFooBar)
suite2 = suite_loader.loadTestsFromTestCase(TestHelloWorld)
suite = unittest.TestSuite([suite1, suite2])
unittest.TextTestRunner(verbosity=2).run(suite)
