from abc import ABC
from enum import Enum

class Size(Enum):
    SMALL = 'small',
    MEDIUM = 'medium'
    LARGE = 'large'
    XLARGE = 'xlarge'

class Topping:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name
    
class PizzaSize:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name
    
class Menu:
    def __init__(self):
        self._toppings = {}
        self._pizzaSize = {}

    def add_topping(self, topping):
        if topping.get_name() not in self._toppings:
            self.toppings[topping.get_name()] = topping

    def add_size(self, size):
        if size.get_name() not in self._pizzaSize:
            self._pizzaSize[size.get_name()] = size

    def get_topping(self, topping):
        self._toppings.get(topping.get_name(), None)

    def get_size(self, size):
        self._pizzaSize.get(size.get_name(), None)
        
    def get_all_toppings(self):
        return self._toppings.values()
    
    def get_all_sizes(self):
        return self._pizzaSize.values()
    
class Pizza:
    def __init__(self, size):
        self._size = size
        self._toppings = {}

    def add_topping(self, topping):
        if topping.get_name() not in self._toppings:
            self.toppings[topping.get_name()] = topping
    
    def remove_topping(self, topping):
        if topping.get_name() in self._toppings:
            del self.toppings[topping.get_name()]

    def calculate_cost(self):
        total = 0
        for topping in self._toppings.values():
            total += topping.get_price()

        return total
    
class Order:
    def __init__(self):
        self._orders = []

    def add_pizza(self, pizza):
        self._orders.append(pizza)

    def remove_pizza(self, i):
        del self._orders[i]

    def calculate_total(self):
        total = 0
        for pizza in self._orders:
            total += pizza.calculate_cost()

        return total
    
    
