from decimal import Decimal
from random import randrange, shuffle

from location import Location


class Board:
    def __init__(self, players):
        self.locations = [
            Location(
                cost_of_sale=randrange(Decimal(50), Decimal(300)),
                cost_of_rent=randrange(Decimal(15), Decimal(90)),
            )
            for _ in range(1, 21)
        ]
        self.players_order = players
        shuffle(self.players_order)
        self.players_location = {player: 0 for player in self.players_order}

    def update_player_location(self, player):
        self.players_location[player] = (
            self.players_location[player] + player.roll_the_dices()
        ) % len(self.locations)

    def remove_losers(self, losers):
        self.players_order = [
            player for player in self.players_order if player not in losers
        ]
        for loser in losers:
            self.players_location.pop(loser)

        for location in self.locations:
            if location.owner in losers:
                location.remove_owner

    def update_player_balance(self, player):
        bonus_value = Decimal(100)
        player.update_balance(bonus_value)

    def get_winner(self):
        balance_rank = {
            player.balance: player for player in self.players_order
        }

        winner = balance_rank.get(max(balance_rank.keys()))
        return winner
