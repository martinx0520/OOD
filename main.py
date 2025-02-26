from abc import ABC
from enum import Enum

class Size(Enum):
    SMALL = 'small',
    MEDIUM = 'medium'
    LARGE = 'large'
    XLARGE = 'xlarge'

class Topping:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
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
    def __init__(self, id, size):
        self._id = id
        self._size = size
        self._toppings = {}

    def get_id(self):
        return self._id
    
    def add_topping(self, topping):
        if topping.get_id() not in self._toppings:
            self.toppings[topping.get_id()] = topping
    
    def remove_topping(self, id):
        if id in self._toppings:
            del self.toppings[id]

    def calculate_cost(self):
        total = self._size.get_price()
        for topping in self._toppings.values():
            total += topping.get_price()

        return total
    
class Order:
    def __init__(self):
        self._orders = {}

    def add_pizza(self, pizza):
        if pizza.get_id() not in self.orders:
            self._orders[pizza.get_id()] = pizza

    def remove_pizza(self, id):
        del self._orders[id]

    def add_topping(self, pizza_id, topping):
        self._orders[pizza_id].add_topping(topping)

    def remove_topping(self, pizza_id, topping_id):
        self._orders[pizza_id].remove_topping(topping_id)

    def calculate_total(self):
        total = 0
        for pizza in self._orders:
            total += pizza.calculate_cost()

        return total
    

