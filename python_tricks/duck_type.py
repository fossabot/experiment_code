# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-26 20:06:50
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-26 20:07:47
class Duck:
    def quack(self):
        print "這鴨子在呱呱叫"
    def feathers(self):
        print "這鴨子擁有白色與灰色羽毛"

class Person:
    def quack(self):
        print "這人正在模仿鴨子"
    def feathers(self):
        print "這人在地上拿起1根羽毛然後給其他人看"

def in_the_forest(d):
    d.quack()
    d.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()
