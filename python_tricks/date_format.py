# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-09 21:03:21
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-09 21:10:48

from datetime import date

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self,code):
        fmt = _formats.get(code,_formats.get('ymd'))
        return fmt.format(d=self)

if __name__ == '__main__':
    d = Date(2017,9,8)
    print format(d,'dmy')
    dd = date(2017,9,8)
    print format(dd,'%A, %B %d,%Y')

