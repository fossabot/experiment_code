# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-12-29 20:51:48
# @Last Modified by:   jerry
# @Last Modified time: 2017-12-29 20:51:52

import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)
