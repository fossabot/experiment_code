# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-09 21:21:21
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-09 21:30:02

class Person:
    def __init__(self,first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self.first_name

    # Setter function
    @first_name.setter
    def first_name(self,value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self.first_name = value

    # Delter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can not delete attribute')

if __name__ == '__main__':
    a = Person("42")
    print a.first_name
    a.first_name = 42


