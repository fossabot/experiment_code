# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-08-22 12:40:52
# @Last Modified by:   jerry
# @Last Modified time: 2017-08-22 13:19:58


from __future__ import print_function
from collections import defaultdict


data = [
        ("animal", "bear"),
        ("animal", "duck"),
        ("plant", "cactus"),
        ("vehicle", "speed boat"),
        ("vehicle", "school bus")
    ]

def a():
    groups = {}
    for (key, value) in data:
        groups.setdefault(key, []).append(value)

    print (groups)

def b():
    groups = defaultdict(list)
    for (key, value) in data:
        groups[key].append(value)
    print (groups)

def c():
    keys = {'a', 'e', 'i', 'o', 'u' }
    value = []
    d = dict.fromkeys(keys, value)
    print(d)

if __name__ == '__main__':
    a()
    b()
    c()

