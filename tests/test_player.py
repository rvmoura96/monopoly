from unittest import TestCase, mock

from monopoly.behaviour import Demanding
from monopoly.location import Location
from monopoly.player import Player


class TestPlayer(TestCase):
    @mock.patch("monopoly.player.randrange", return_value=6)
    def test_player_roll_the_dices_should_return_6(
        self, mocked_choice
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        result = player.roll_the_dices()
        expected = 6
        self.assertEqual(expected, result, 'message')

    def test_update_balance_should_update_the_player_balance_with_the_parameter_value(self):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        player.update_balance(50)
        expected = 350
        result = player.balance
        self.assertEqual(expected, result, 'message')
