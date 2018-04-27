# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-27 10:18:40
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-27 10:26:51

import pytest

# setup
@pytest.fixture(scope="session")
def count():
    """
    docstring...
    """
    print("init count")
    return 10 

# teardown
@pytest.fixture(scope="session")
def count2():
    """
    tear down
    """
    print('teardown count')
    yield 1000
    print('teardown count')
