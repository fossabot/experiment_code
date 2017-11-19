#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 14:57
# @Author  : Zhiwei Yang
# @File    : factory_method.py.py


"""
工厂方法集中的在一个地方创建对象，使对象的跟踪变得更容易。
工厂方法模式可以帮助我们将产品的实现从使用中解耦。如果增加产品或者改变产品的实现，Creator 并不会收到影响。
使用工厂方法模式的另一个优点是在系统中加入新产品时，无须修改抽象工厂和抽象产品提供的接口，无须修改客户端，
也无须修改其他的具体工厂和具体产品，而只要添加一个具体工厂和具体产品就可以了。这样，系统的可扩展性也就变得非常好，
完全符合“开闭原则”。
"""

class Pizza:
    name = None
    dough = None
    sauce = None
    toppings = []

    def prepare(self):
        print("preparing %s" % self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(" %s"% topping)

    def bake(self):
        print("Bake for 25 minutes at 350.")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def __str__(self):
        return self.name

class PizzaStore:
    def create_pizza(self,pizza_type):

        # 每个需要子类实现的方法都会抛出NotImplementedError
        # 我们也可以把 PizzaStore 的 metaclass 设置成 abc.ABCMeta
        # 这样的话，这个类就是真正的抽象基类
        raise NotImplementedError()

    def order_pizza(self,pizza_type):
        pizza = self.create_pizza(pizza_type)

        #  一旦我们有了一个 pizza，需要做一些准备（擀面皮、加佐料），然后烘烤、切片、装盒
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYStyleCheesePizza(Pizza):
    name = "NY Style Sauce and Cheese Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated", "Reggiano", "Cheese"]



class ChicagoCheesePizza(Pizza):
    name = "Chicago Style Deep Dish Cheese Pizza"
    dough = "Extra Thick Crust Dough"
    sauce = "Plum Tomato Sauce"
    toppings = ["Shredded", "Mozzarella", "Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices")



class NYStylePizzaStore(PizzaStore):
    def create_pizza(self,pizza_type):
        # 根据 pizza 类型，我们实例化正确的具体类，然后将其赋值给 pizza 实例变量
        if pizza_type == "cheese":
            pizza = NYStyleCheesePizza()

        return pizza

class ChicagoCheeseStore(PizzaStore):
    def create_pizza(self,pizza_type):
        if pizza_type == "cheese":
            pizza = ChicagoCheesePizza()

        return pizza


def main():
    nystore = NYStylePizzaStore()
    pizza = nystore.order_pizza("cheese")
    print("goodspeed ordered a %s" % pizza)
    print("*" * 10)


    chicagostore = ChicagoCheeseStore()
    pizza_chicago = chicagostore.order_pizza("cheese")
    print("chicago ordered a %s" % pizza_chicago)
    print("*" * 10 )


if __name__ == '__main__':
    main()

