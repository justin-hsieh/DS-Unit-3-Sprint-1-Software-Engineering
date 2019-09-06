# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:03:53 2019

@author: showi
"""
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_prod=30):

    products = []

    for _ in list(range(num_prod)):

        first = sample(ADJECTIVES, 1)
        last = sample(NOUNS, 1)
        firstlast = first.append(' '.join(last))

        prod = Product(name=firstlast)

        prod.price = randint(5, 101)
        prod.weight = randint(5, 101)
        prod.flammability = uniform(0.0, 2.5)

        products.append(prod)

    return products


def inventory_report(prods):

        unique = len(prods)
        total_price = 0
        total_weight = 0
        total_flam = 0

        for prod in prods:

            total_price += prod.price
            total_weight += prod.weight
            total_flam += prod.flammability

        ave_price = total_price / unique
        ave_weight = total_weight / unique
        ave_flam = total_flam / unique

        print('\n\n ACME CORPORATION OFFICIAL INVENTORY REPORT \n')
        print(f'Unique product names: {unique}\n')
        print(f'Average Price: {ave_price:.1f}\n')
        print(f'Average Weight: {ave_weight:.1f}\n')
        print(f'Average Flammability: {ave_flam:.1f}\n')


if __name__ == '__main__':
    inventory_report(generate_products())

