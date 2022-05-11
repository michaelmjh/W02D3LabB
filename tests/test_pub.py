import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("josh", 27, 10, 0)
        self.customer_2 = Customer("michael", 38, 0, 12)
        self.customer_3 = Customer("steve", 40, 10, 20)
        self.customer_4 = Customer("ethan", 3, 10, 0)

        self.drink_1 = Drink("beer", 4, 5)
        self.drink_2 = Drink("wine", 5, 12)
        self.drink_3 = Drink("whiskey", 6, 40)

        self.food_1 = Food("pizza", 5, 2)

        stock = {
            self.drink_1: 3,
            self.drink_2: 0,
            self.drink_3: 10
        }

        self.pub = Pub("The Pub", 100, stock)

    def test_get_name(self):
        self.assertEqual("The Pub", self.pub.name)


    def test_get_till(self):
        self.assertEqual(100, self.pub.till)


    def test_increase_till(self):
        self.pub.increase_till(self.drink_1)
        self.assertEqual(104, self.pub.till)


    def test_decrease_stock_pass(self):
        self.pub.decrease_stock(self.drink_1)
        self.assertEqual(2, self.pub.stock[self.drink_1])


    def test_decrease_stock_fail(self):
        self.pub.decrease_stock(self.drink_2)
        self.assertEqual(0, self.pub.stock[self.drink_2])


    def test_drink_in_stock_true(self):
        in_stock = self.pub.check_in_stock(self.drink_1)
        self.assertEqual(True, in_stock)


    def test_check_stock_value(self):
        self.assertEqual(72 ,self.pub.check_stock_value())


    def test_check_stock_value_after_sale(self):
        self.pub.decrease_stock(self.drink_1)
        self.assertEqual(68 ,self.pub.check_stock_value())


    def test_under_drinking_limit_pass(self):
        under_limit = self.pub.check_under_drinking_limit(self.customer_1)
        self.assertEqual(True, under_limit)


    def test_under_drinking_limit_fail(self):
        under_limit = self.pub.check_under_drinking_limit(self.customer_3)
        self.assertEqual(False, under_limit)


    def test_over_age_limit_pass(self):
        over_age = self.pub.check_age(self.customer_1)
        self.assertEqual(True, over_age)


    def test_over_age_limit_fail(self):
        over_age = self.pub.check_age(self.customer_4)
        self.assertEqual(False, over_age)


    def test_buy_drink(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(68 ,self.pub.check_stock_value())
        self.assertEqual(104, self.pub.till)
        self.assertEqual(6, self.customer_1.wallet)
        self.assertEqual(5, self.customer_1.intoxication)


    def test_buy_drink_cant_afford(self):
        self.pub.sell_drink(self.drink_1, self.customer_2)
        self.assertEqual(72 ,self.pub.check_stock_value())
        self.assertEqual(100, self.pub.till)
        self.assertEqual(0, self.customer_2.wallet)
        self.assertEqual(12, self.customer_2.intoxication)


    def test_buy_drink_over_limit(self):
        self.pub.sell_drink(self.drink_1, self.customer_3)
        self.assertEqual(72 ,self.pub.check_stock_value())
        self.assertEqual(100, self.pub.till)
        self.assertEqual(10, self.customer_3.wallet)
        self.assertEqual(20, self.customer_3.intoxication)


    def test_buy_drink_under_age(self):
        self.pub.sell_drink(self.drink_1, self.customer_4)
        self.assertEqual(72 ,self.pub.check_stock_value())
        self.assertEqual(100, self.pub.till)
        self.assertEqual(10, self.customer_4.wallet)
        self.assertEqual(0, self.customer_4.intoxication)


    def test_buy_food_no_intoxication(self):
        self.pub.sell_food(self.food_1, self.customer_1)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(5, self.customer_1.wallet)
        self.assertEqual(0, self.customer_1.intoxication)


    def test_buy_food_lower_intoxication(self):
        self.pub.sell_food(self.food_1, self.customer_3)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(5, self.customer_3.wallet)
        self.assertEqual(18, self.customer_3.intoxication)

    
    def test_buy_food_cant_afford(self):
        self.pub.sell_food(self.food_1, self.customer_2)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(0, self.customer_2.wallet)
        self.assertEqual(12, self.customer_2.intoxication)