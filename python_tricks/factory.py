#! -*- coding: utf-8 -*-

"""
抽象工厂模式
"""


# 原料

class FreshClams:

    def __str__(self):
        return 'Fresh Clams'


class MarinaraSauce:

    def __str__(self):
        return "Marinara Sauce"


class ThickCrustDough:

    def __str__(self):
        return "Thick Crust Dough"


class ReggianoCheese:

    def __str__(self):
        return "Reggiano Cheese"


class SlicedPepperoni:

    def __str__(self):
        return "Sliced Pepperoni"


class Garlic:

    def __str__(self):
        return "Garlic"


class Onion:

    def __str__(self):
        return "Onion"


class RedPepper:

    def __str__(self):
        return "Red Pepper"


class PizzaIngredientFactory:

    '''
    定义原料工厂
    '''

    def create_dough(self):
        raise NotImplementedError()

    def create_sauce(self):
        raise NotImplementedError()

    def create_cheese(self):
        raise NotImplementedError()

    def create_pepperoni(self):
        raise NotImplementedError()

    def create_clam(self):
        raise NotImplementedError()

    def create_veggies(self):
        raise NotImplementedError()


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        print("Tossing %s" % ThickCrustDough())
        return ThickCrustDough()

    def create_sauce(self):
        print("Adding %s..." % MarinaraSauce())
        return MarinaraSauce()

    def create_cheese(self):
        print("Adding %s..." % ReggianoCheese())
        return ReggianoCheese()

    def create_pepperoni(self):
        print("Adding %s..." % SlicedPepperoni())
        return SlicedPepperoni()

    def create_clam(self):
        print("Adding %s..." % FreshClams())
        return FreshClams()

    def create_veggies(self):
        veggies = [Garlic(), Onion(), RedPepper()]
        for veggie in veggies:
            print("  %s" % veggie)
        return veggies


class Pizza:

    '''
    pizza 工厂
    '''

    dough = None
    sauce = None
    cheese = None
    veggies = []
    pepperoni = None
    clam = None

    def __init__(self, name, ingredient_factory):
        self.name = name
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        raise NotImplementedError()

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def __str__(self):
        return self.name


class NYStyleCheesePizza(Pizza):

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        clam = self.ingredient_factory.create_clam()
        veggies = self.ingredient_factory.create_veggies()


class NYStyleClamPizza(Pizza):

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        clam = self.ingredient_factory.create_clam()


class PizzaStore:

    '''
    pizza 店工厂
    '''

    ingredient_factory = None

    def create_pizza(self, pizza_type):
        # 每个需要子类实现的方法都会抛出NotImplementedError
        # 我们也可以把 PizzaStore 的 metaclass 设置成 abc.ABCMeta
        # 这样的话，这个类就是真正的抽象基类
        raise NotImplementedError()

    def order_pizza(self, pizza_type):  # 现在把 pizza 的类型传入 order_pizza()

        pizza = self.create_pizza(pizza_type)

        #  一旦我们有了一个 pizza，需要做一些准备（擀面皮、加佐料），然后烘烤、切片、装盒
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    # 下边是其他可能用到的方法


class NYStylePizzStore(PizzaStore):

    ingredient_factory = NYPizzaIngredientFactory()

    def create_pizza(self, pizza_type):
        # 根据 pizza 类型，我们实例化正确的具体类，然后将其赋值给 pizza 实例变量
        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza('NY Style Sauce and Cheese Pizza',
                                       self.ingredient_factory)
        elif pizza_type == 'clam':
            pizza = NYStyleClamPizza('NY Style Clam Pizza',
                                     self.ingredient_factory)
        return pizza


def main():
    nystore = NYStylePizzStore()
    pizza = nystore.order_pizza('cheese')
    print('*' * 10)
    print("goodspeed ordered a %s" % pizza)
    print('*' * 10)

if __name__ == '__main__':
    main()