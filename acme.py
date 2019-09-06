
"""
Created on Fri Sep  6 08:04:12 2019

@author: showi
"""
from random import randint, uniform, sample
import unittest

class Product():

        def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                     identifier=randint(1000000, 10000000)):
            self.name = name
            self.price = price
            self.weight = weight
            self.flammability = flammability
            self.identifier = identifier

        def stealability(self):
            ratio = self.price / self.weight
            if ratio < 0.5:
                return "Not so stealable..."
            elif 0.5 <= ratio < 1.0:
                return "Kinda stealable"
            else:
                return "Very stealable!"

        def explode(self):
            exp = self.flammability * self.weight
            if exp < 10:
                return "...fizzle"
            elif 10 <= exp < 50:
                return "....boom!"
            else:
                return "BABOOM!"


class BoxingGlove(Product):
        def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                     identifier=randint(1000000, 10000000)):
            super().__init__(name, price, weight, flammability, identifier)

        def punch(self):
            if self.weight < 5:
                return "That tickles"
            if 5 <= self.weight < 15:
                return "Hey that hurt!"
            else:
                return "OUCH!"

        def explode(self):
            return "....it's a glove"

prod = Product('A Cool Toy')    
print(prod.explode()) 
glove = BoxingGlove('Punchy the Third')
print(glove.weight)




