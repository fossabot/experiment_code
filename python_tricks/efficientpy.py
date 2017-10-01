# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-01 09:08:46
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-01 09:39:00
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')

def low_efficiency():
    # 创建将0到19连接起来的字符串 (例 "012..1819")
    nums = ""
    for n in range(20):
      nums += str(n)   # 慢且低效
    print nums
def high_efficiency():
    num = ""
    m =[]
    for n in range(20):
        m.append(str(n))
    print "".join(m)

def highest_efficiency():
    nums = map(lambda x:x*x,range(20))
    print nums

# changed list
def append_to(element, to=[]):
    # 这句话读三遍，当函数被定义时，Python的默认参数就被创建 一次，而不是每次调用函数的时候创建。
    # 这句话读三遍， 这意味着，如果你使用一个可变默认参数并改变了它，你 将会 在未来所有对此函数的 调用中改变这个对象。
    to.append(element)
    return to

def append_to_as_None(element, to=None):
    if to is None:
        to = []
    to.append(element)

    return to


if __name__ == '__main__':
    # highest_efficiency()
    my_list = append_to(12)
    print my_list

    my_other_list = append_to(42)
    print my_other_list


    my_list = append_to_as_None(12)
    print my_list

    my_other_list = append_to_as_None(42)
    print my_other_list

