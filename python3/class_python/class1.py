# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-03 13:44:50
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-03 13:54:10

class Base:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def printme(self):    
        print("printme,hahah")
        return self.a + self.b