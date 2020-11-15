from random import randrange


class Player:
    def __init__(self, behaviour, balance):
        self.behaviour = behaviour
        self.balance = balance
        self.position = 0

    def receive_rent(self, cost_of_rent):
        self.balance += cost_of_rent

    def pay_rent(self, location):
        if location.owner and location.owner != self:
            self.balance -= location.cost_of_rent
            location.owner.receive_rent(location.cost_of_rent)

    def buy(self, location):
        if self.behaviour.buy(self, location):
            self.balance -= location.cost_of_sale
            location.update_owner(self)

    def update_balance(self, income):
        self.balance += income

    def roll_the_dices(self):
        return randrange(1, 7)

    def __repr__(self):
        return f'{self.balance} - {self.behaviour.__class__}'
