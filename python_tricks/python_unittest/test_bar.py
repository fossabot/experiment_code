# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 16:01:02
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 16:01:06
from __future__ import print_function

import unittest
import __builtin__

if __name__ == "__main__":
    conf = type('TestConf', (object,), {})
    conf.isskip = True

    # make a cross-module variable
    __builtin__.conf = conf
    module = __import__('test_foo')
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(module.TestFoo)
    unittest.TextTestRunner(verbosity=2).run(suite)
