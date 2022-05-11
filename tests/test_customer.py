import unittest

from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("josh", 27, 10, 0)
        self.customer_2 = Customer("michael", 38, 0, 12)
        self.customer_3 = Customer("steve", 40, 10, 20)
        self.customer_4 = Customer("ethan", 3, 10, 0)

        self.drink_1 = Drink("beer", 4, 5)

        self.food_1 = Food("pizza", 5, 2)


    def test_get_name(self):
        self.assertEqual("josh", self.customer_1.name)


    def test_get_wallet(self):
        self.assertEqual(10, self.customer_1.wallet)


    def test_check_can_afford_true(self):
        can_afford = self.customer_1.can_afford(self.drink_1)
        self.assertEqual(True, can_afford)


    def test_check_can_afford_false(self):
        can_afford = self.customer_2.can_afford(self.drink_1)
        self.assertEqual(False, can_afford)


    def test_increase_intoxication(self):
        self.customer_1.increase_intoxication(self.drink_1)
        self.assertEqual(5, self.customer_1.intoxication)


    def test_decrease_intoxication(self):
        self.customer_2.decrease_intoxication(self.food_1)
        self.assertEqual(10, self.customer_2.intoxication)


    def test_decrease_wallet(self):
        self.customer_1.decrease_wallet(self.drink_1)