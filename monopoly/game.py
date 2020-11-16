from collections import Counter
from decimal import Decimal
from random import randrange, shuffle
from statistics import mean

from behaviour import Cautious, Demanding, Impulsive, Random
from board import Board
from location import Location
from player import Player

simulations = 0
winners = []
hist_turns = []
timeout_victories = 0

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
        for player in board.players_order:
            player_initial_position = board.players_location.get(player)
            board.update_player_location(player)
            if board.players_location.get(player) <= player_initial_position:
                board.update_player_balance(player)
            player.buy(board.locations[board.players_location.get(player)])
            player.pay_rent(board.locations[board.players_location.get(player)])
            if player.balance <= 0 and len(board.players_order) > 1:
                board.remove_losers([player])
        if len(board.players_order) == 1:
            winner = board.get_winner()
            break
        turns += 1
    else:
        winner = board.get_winner()
        timeout_victories += 1

    winners.append(winner)
    simulations += 1
    hist_turns.append(turns)
behaviours_victories = Counter(str(w.behaviour) for w in winners)
behaviours_percs = {
    key: (value / simulations) * 100 for key, value in behaviours_victories.items()
}
most_behavior_victories = behaviours_victories.most_common(1)[0]

print(
    f"Comportamento com maior taxa de vitorias - {most_behavior_victories[0]} = {behaviours_percs.get(most_behavior_victories[0])}"
)
print(
    f"Comportamentos e suas porcentagens de vitorias em todas as simulações = {behaviours_percs=}"
)

print(f"Média de turnos = {mean(hist_turns)=}")
print(f"Vitórias por timeout = {timeout_victories=}")
