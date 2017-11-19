#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/19 23:41
# @Author  : Zhiwei Yang
# @File    : python-design-patter-build-mode.py

#! -*- coding: utf-8 -*-

"""
建造者模式
"""

import time


STEP_DELAY = 0.1

PIZZA_PROGRESS = ['prepare', 'bake', 'cut', 'box']


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare_dough(self, dough):
        self.dough = dough
        print(self.dough)
        print('preparing the {} dough of your {}...'.format(self.dough, self))
        time.sleep(STEP_DELAY)
        print('Done with the {} dough'.format(self.dough))

    def __str__(self):
        return self.name


class PizzaBuilder(object):

    name = None

    def __init__(self):
        self.progress = PIZZA_PROGRESS
        self.baking_time = 5

    def prepare_dough(self):
        raise NotImplementedError()

    def add_sauce(self):
        raise NotImplementedError()

    def add_topping(self):
        raise NotImplementedError()

    def bake(self):
        raise NotImplementedError()

    def cut(self):
        raise NotImplementedError()

    def box(self):
        raise NotImplementedError()

    @property
    def pizza(self):
        return Pizza(self.name)


class NYStyleCheeseBuilder(PizzaBuilder):

    name = 'NY Style Sauce and Cheese Pizza'

    def prepare_dough(self):
        self.progress = PIZZA_PROGRESS[0]
        self.pizza.prepare_dough('thin')

    def add_sauce(self):
        print('adding the tomato sauce to your pizza..')
        self.pizza.sauce = 'tomato'
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (grated reggiano cheese) to your pizza')
        self.pizza.toppings.append(["Grated", "Reggiano", "Cheese"])
        time.sleep(STEP_DELAY)
        print('done with the topping (grated reggiano cheese)')

    def bake(self):
        self.progress = PIZZA_PROGRESS[1]
        print('baking your pizza for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)

    def cut(self):
        self.progress = PIZZA_PROGRESS[2]
        print("Cutting the pizza into diagonal slices")

    def box(self):
        self.progress = PIZZA_PROGRESS[3]
        print("Place pizza in official PizzaStore box")


class ChicagoStyleCheeseBuilder(PizzaBuilder):

    name = 'Chicago Style Deep Dish Cheese Pizza'

    def prepare_dough(self):
        self.progress = PIZZA_PROGRESS[0]
        self.pizza.prepare_dough('cheese')

    def add_sauce(self):
        print('adding the dish sauce to your pizza..')
        self.pizza.sauce = 'dish'
        time.sleep(STEP_DELAY)
        print('done with the dish sauce')

    def add_topping(self):
        print('adding the topping (Shredded, Mozzarella, Cheese) to your pizza')
        self.pizza.toppings.append(["Shredded", "Mozzarella", "Cheese"])
        time.sleep(STEP_DELAY)
        print('done with the topping (Shredded, Mozzarella, Cheese)')

    def bake(self):
        self.progress = PIZZA_PROGRESS[1]
        print('baking your pizza for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)

    def cut(self):
        self.progress = PIZZA_PROGRESS[2]
        print("Cutting the pizza into diagonal slices")

    def box(self):
        self.progress = PIZZA_PROGRESS[3]
        print("Place pizza in official PizzaStore box")


class Waiter:
    # 指挥者

    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        #  一旦我们有了一个 pizza，需要做一些准备（擀面皮、加佐料），然后烘烤、切片、装盒
        [step() for step in (builder.prepare_dough, builder.add_sauce,
                             builder.add_topping, builder.bake,
                             builder.cut, builder.box)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like, [N]YStyleCheesePizza or [C]hicagoStyleCheesePizza?')
        builder = builders[pizza_style]
    except KeyError as err:
        print('Sorry, only NYStyleCheesePizza and ChicagoStyleCheesePizza are avaliable')
        return False, None
    return True, builder


def main():
    builders = dict(N=NYStyleCheeseBuilder, C=ChicagoStyleCheeseBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    waiter = Waiter()
    waiter.construct_pizza(builder())
    pizza = waiter.pizza
    print('Enjoy your {}!'.format(pizza))


if __name__ == '__main__':
    main()