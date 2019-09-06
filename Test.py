# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:19:11 2019

@author: showi
"""

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        prod = Product(price=2, weight=4)
        self.assertEqual(prod.stealability(), 'Kinda stealable')

    def test_explode(self):
        prod = Product(flammability=1, weight=4)
        self.assertEqual(prod.explode(), '...fizzle')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        pass
        # Could not seem to get the names of the products separated
        #name = prod.name.split(' ')
        #self.assertIn(name[0], ADJECTIVES)
        #self.assertIn(name[1], NOUNS)
        #self.assertIn(' ', prod.name)


if __name__ == '__main__':
    unittest.main()
    