from __future__ import print_function

import unittest

print(conf)

class TestFoo(unittest.TestCase):
    """Cross-module variables to Test files

    [description]

    Extends:
        unittest.TestCase

    Variables:
        print(conf) {[type]} -- [description]
    """
    def test_foo(self):
        print(conf)

    @unittest.skipIf(conf.isskip==True, "skip test")
    def test_skip(self):
        raise RuntimeError

