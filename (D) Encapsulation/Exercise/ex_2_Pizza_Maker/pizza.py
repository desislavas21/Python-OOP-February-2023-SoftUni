from Exercise.ex_2_Pizza_Maker.dough import Dough
from typing import Dict
from Exercise.ex_2_Pizza_Maker.topping import Topping

class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str: float] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) < self.max_number_of_toppings:
            if topping.topping_type not in self.toppings.keys():
                self.toppings[topping.topping_type] = topping.weight
            else:
                self.toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return sum(self.toppings.values()) + self.dough.weight
