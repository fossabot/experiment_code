# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2018-02-01 22:57:12
# @Last Modified by:   jerry

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


"""
from logbook import Logger, StreamHandler
import sys
StreamHandler(sys.stdout).push_application()
log = Logger("My Awesome logger")
log.warn("This is too cool for stdlibrary")
"""

import os
from time import sleep
import logbook
from logbook.more import ColorizedStderrHandler
print(os.path.abspath(''))
path = '.'
LOG_DIR = os.path.join(path, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
def get_logger(name='Test', file_log=True, level=None):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    if file_log:
        logbook.TimedRotatingFileHandler(os.path.join(LOG_DIR, '%s.log' % name),
                                         date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)
LOG = get_logger(file_log=True, level='INFO')

if __name__ == "__main__":
    for item in range(1000):
        LOG.info('Log-info')
        sleep(0.5)

