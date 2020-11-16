from abc import ABC, abstractmethod
from random import choice


class Behaviour(ABC):
    def buy(self, player, location):
        if player.balance >= location.cost_of_sale and not location.owner:
            return self.behave(player, location)
        return False

    @abstractmethod
    def behave(self, player, location):
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}"


class Impulsive(Behaviour):
    def behave(self, player, location):
        return True


class Demanding(Behaviour):
    def behave(self, player, location):
        return location.cost_of_rent > 50


class Cautious(Behaviour):
    def behave(self, player, location):
        return player.balance - location.cost_of_sale >= 80


class Random(Behaviour):
    def behave(self, player, location):
        return choice([True, False])
