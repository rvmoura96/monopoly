from collections import Counter
from decimal import Decimal
from random import randrange, shuffle

from behaviour import Cautious, Demanding, Impulsive, Random
from board import Board
from location import Location
from player import Player


simulations = 0
winners = []
while simulations < 300:
    cautious, demading, impulsive, random = (
        Cautious(),
        Demanding(),
        Impulsive(),
        Random(),
    )
    player, player2, player3, player4 = (
        Player(impulsive, Decimal(300)),
        Player(demading, Decimal(300)),
        Player(cautious, Decimal(300)),
        Player(random, Decimal(300)),
    )

    board = Board([player, player2, player3, player4])
    turns = 1

    while turns <= 1000 and len(board.players_order) > 1:
        print(f'{simulations=} - {turns=} - {board.players_order=}')
        for player in board.players_order:
            player_initial_position = board.players_location.get(player)
            board.update_player_location(player)
            if board.players_location.get(player) <= player_initial_position:
                board.update_player_balance(player)
            player.buy(board.locations[board.players_location.get(player)])
            player.pay_rent(
                board.locations[board.players_location.get(player)]
            )
            if player.balance < 0:
                board.remove_losers([player])
        if len(board.players_order) == 1:
            winner = board.get_winner()
            print(f'turns: {turns} - {winner}')
            break
        turns += 1
    else:
        winner = board.get_winner()

    winners.append(winner)
    simulations += 1

print(Counter(type(w.behaviour) for w in winners).most_common(1))
