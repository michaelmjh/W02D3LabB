class Pub:
    def __init__(self, name, till, stock):
        self.name = name
        self.till = till
        self.stock = stock

    def increase_till(self, consumable):
        self.till += consumable.price

    def check_in_stock(self, drink):
        if self.stock[drink] > 0:
            return True
        else:
            return False

    def decrease_stock(self, drink):
        if self.stock[drink] > 0:
            self.stock[drink] -= 1

    def check_stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink.price * self.stock[drink])
        return total
            

    def check_under_drinking_limit(self, customer):
        if customer.intoxication < 15:
            return True
        else:
            return False

    
    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False
            

    def sell_drink(self, drink, customer):
        in_stock = self.check_in_stock(drink)
        over_age = self.check_age(customer)
        under_limit = self.check_under_drinking_limit(customer)

        can_afford = customer.can_afford(drink)

        if in_stock and over_age and under_limit and can_afford:
            self.decrease_stock(drink)
            self.increase_till(drink)
            customer.decrease_wallet(drink)
            customer.increase_intoxication(drink)


    def sell_food(self, food, customer):
        can_afford = customer.can_afford(food)

        if can_afford:
            self.increase_till(food)
            customer.decrease_wallet(food)
            customer.decrease_intoxication(food)