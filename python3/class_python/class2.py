# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-03 13:46:22
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-03 14:48:41

from class1 import Base

class Checkusebasevar(Base):
    
    def __init__(self):
        self.vc = Base.printme()

    def printtwo(self):
        # print (self.a,self.b)
        
        print (self.vc)
        # print (self.c)

if __name__ == '__main__':
    
    bb = Checkusebasevar(1,3)
    bb.printtwo()
    
    # print (bb.printme())

