# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 16:15:41
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 16:16:34

import unittest
import doctest

"""
This is an example of doctest

>>> fib(10)
55
"""

def fib(n):
    """ This function calculate fib number.

    Example:

        >>> fib(10)
        55
        >>> fib(-1)
        Traceback (most recent call last):
            ...
        ValueError
    """
    if n < 0:
        raise ValueError('')
    return 1 if n<=2 else fib(n-1) + fib(n-2)

if __name__ == "__main__":
    finder = doctest.DocTestFinder()
    suite = doctest.DocTestSuite(test_finder=finder)
    unittest.TextTestRunner(verbosity=2).run(suite)
