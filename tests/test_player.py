from unittest import TestCase, mock

from monopoly.behaviour import Demanding, Impulsive, Random
from monopoly.location import Location
from monopoly.player import Player


class TestPlayer(TestCase):
    def test_player_buy_property_when_impulsive_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_no_owner_should_update_player_balance(
        self,
    ):
        behaviour = Impulsive()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=150)
        player.buy(location)
        result = player.balance
        expected_balance = 150
        self.assertEqual(expected_balance, result, "message")

    def test_player_buy_property_when_impulsive_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_owner_should_keep_player_balance_unchanged(
        self,
    ):
        behaviour = Impulsive()
        player = Player(behaviour=behaviour, balance=300)
        player2 = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=150)
        location.owner = player2
        expected = 300
        player.buy(location)
        result = player.balance
        self.assertEqual(expected, result, "message")

    def test_player_buy_property_when_impulsive_behaviour_and_balance_lesser_than_property_cost_of_sale_and_property_has_no_owner_should_keep_player_balance_unchanged(
        self,
    ):
        behaviour = Impulsive()
        player = Player(behaviour=behaviour, balance=100)
        location = Location(cost_of_sale=150, cost_of_rent=150)
        expected = 100
        player.buy(location)
        result = player.balance
        self.assertEqual(expected, result, "message")

    def test_player_buy_property_when_demanding_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_no_owner_should_update_player_balance(
        self,
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=51)
        expected = 150
        player.buy(location)
        result = player.balance
        self.assertEqual(expected, result, "message")

    def test_player_buy_property_when_demanding_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_no_owner_and_cost_of_rent_lesser_than_50_should_keep_player_balance_unchanged(
        self,
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=49)
        expected = 300
        player.buy(location)
        result = player.balance
        self.assertEqual(expected, result, "message")

    def test_player_buy_property_when_demanding_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_no_owner_and_cost_of_rent_lesser_than_50_should_keep_player_balance_unchanged(
        self,
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        player2 = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=49)
        expected = 300
        player.buy(location)
        result = player.balance
        self.assertEqual(expected, result, "message")

    @mock.patch("monopoly.behaviour.choice", return_value=True)
    def test_player_buy_property_when_random_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_no_owner_and_random_choice_mock_true_player_balance_should_be_updated(
        self, mocked_choice
    ):
        behaviour = Random()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=49)
        player.buy(location)
        expected = 150
        result = player.balance
        self.assertEqual(expected, result, "message")

    @mock.patch("monopoly.behaviour.choice", return_value=False)
    def test_player_buy_property_when_random_behaviour_and_balance_greater_than_property_cost_of_sale_and_property_has_no_owner_and_random_choice_mock_false_player_balance_should_be_unchanged(
        self, mocked_choice
    ):
        behaviour = Random()
        player = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=49)
        player.buy(location)
        expected = 300
        result = player.balance
        self.assertEqual(expected, result, "message")

    def test_player_pay_rent_should_update_player_balance_when_location_has_owner(
        self,
    ):
        behaviour = Demanding()
        player = Player(behaviour=behaviour, balance=300)
        player2 = Player(behaviour=behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=50)
        location.owner = player2
        player_expected_balance = 250
        player2_expected_balance = 350
        player.pay_rent(location)
        self.assertEqual(player.balance, player_expected_balance)
        self.assertEqual(player2.balance, player2_expected_balance)
