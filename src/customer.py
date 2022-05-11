class Customer:
    def __init__(self, name, age, wallet, intoxication_level):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.intoxication = intoxication_level


    def can_afford(self, consumable):
        if self.wallet >= consumable.price:
            return True
        else:
            return False


    def decrease_wallet(self, consumable):
        self.wallet -= consumable.price


    def increase_intoxication(self, drink):
        self.intoxication += drink.alcohol_level


    def decrease_intoxication(self, food):
        self.intoxication -= food.rejuvination_level
        if self.intoxication <= 0:
            self.intoxication = 0

