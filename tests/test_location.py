from unittest import TestCase

from monopoly.behaviour import Demanding
from monopoly.location import Location
from monopoly.player import Player


class TestLocation(TestCase):
    def test_player_pay_rent_should_update_player_balance_when_location_has_owner(
        self,
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        player2 = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=50)
        location.update_owner(player2)
        player_expected_balance = 250
        player2_expected_balance = 350
        player.pay_rent(location)
        self.assertEqual(player.balance, player_expected_balance)
        self.assertEqual(player2.balance, player2_expected_balance)

    def test_update_owner_should_set_player_as_location_owner_value(self):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=50)
        location.update_owner(player)
        result = location.owner
        expected = player
        self.assertEqual(expected, result, "message")

    def test_remove_owner_should_set_location_owner_value_to_none(self):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=50)
        location.update_owner(player)
        location.remove_owner()
        self.assertIsNone(location.owner)

    def test_repr_should_return_a_string_with_player_info_and_location_cost_of_sale_and_location_cost_of_rent(
        self,
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=50)
        location.update_owner(player)
        expected = "300 - Demanding - 150 - 50"
        result = repr(location)
        self.assertEqual(expected, result)
