# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2017-12-12 13:52:04
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2017-12-12 13:57:43

from collections import namedtuple

# 定义一个namedtuple类型User，并包含name，sex和age属性。
User =namedtuple('User',['name','sex','age'])

# 创建一个User对象
user1 = User(name='yang',sex='Male',age=13)

# 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
user2 = User._make(['zhiwei','male',18])

print user1,user2
print user2.name

# 修改对象属性，注意要使用"_replace"方法

user1 = user1._replace(age=22)
print user1
print user2._asdict().get('name')

dic = {i:2*i for i in range(3)}
print dic

dic1 = dict.fromkeys(range(3), range(3))

print dic1
