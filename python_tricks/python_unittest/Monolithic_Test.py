# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 15:59:14
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 15:59:38

from __future__ import print_function
import unittest

class Monolithic(unittest.TestCase):
    def step1(self):
        print('step1')
    def step2(self):
        print('step2')
    def step3(self):
        print('step3')
    def _steps(self):
        for attr in sorted(dir(self)):
            if not attr.startswith('step'):
                continue
            yield attr
    def test_foo(self):
        for _s in self._steps():
            try:
                getattr(self, _s)()
            except Exception as e:
                self.fail('{} failed({})'.format(attr, e))

suite = unittest.TestLoader().loadTestsFromTestCase(Monolithic)
unittest.TextTestRunner().run(suite)
