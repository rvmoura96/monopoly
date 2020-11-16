from unittest import TestCase, mock

from monopoly.behaviour import Cautious, Demanding, Impulsive, Random
from monopoly.location import Location
from monopoly.player import Player


class TestImpulsiveBehaviour(TestCase):
    def setUp(self):
        self.behaviour = Impulsive()
        self.player = Player(behaviour=self.behaviour, balance=300)

    def test_impulsive_behaviour_buy_should_return_true_when_player_balance_is_greater_than_location_cost_of_sale_and_location_has_no_owner(
        self,
    ):
        location = Location(cost_of_sale=150, cost_of_rent=150)
        self.player.buy(location)
        result = self.player.balance
        expected_balance = 150
        self.assertEqual(expected_balance, result, "message")

    def test_impulsive_behaviour_buy_should_keep_balance_attribute_when_a_property_already_have_a_owner(
        self,
    ):
        player2 = Player(behaviour=self.behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=150)
        location.owner = player2
        expected = 300
        self.player.buy(location)
        result = self.player.balance
        self.assertEqual(expected, result, "message")

    def test_impulsive_behaviour_buy_should_keep_balance_attribute_when_a_property_cost_of_sale_is_greater_than_player_balance(
        self,
    ):
        location = Location(cost_of_sale=150, cost_of_rent=150)
        expected = 150
        self.player.buy(location)
        result = self.player.balance
        self.assertEqual(expected, result, "message")


class TestDemandingBehaviour(TestCase):
    def setUp(self):
        self.behaviour = Demanding()
        self.player = Player(behaviour=self.behaviour, balance=300)

    def test_demanding_behaviour_buy_should_update_player_balance_when_location_cost_of_saler_lesser_than_player_balance_and_location_cost_of_rent_greater_than_50(
        self,
    ):
        location = Location(cost_of_sale=150, cost_of_rent=51)
        expected = 150
        self.player.buy(location)
        result = self.player.balance
        self.assertEqual(expected, result, "message")

    def test_demanding_behaviour_buy_should_keep_player_balance_when_location_cost_of_rent_lesser_than_50(
        self,
    ):
        location = Location(cost_of_sale=150, cost_of_rent=49)
        expected = 300
        self.player.buy(location)
        result = self.player.balance
        self.assertEqual(expected, result)

    def test_demanding_behaviour_buy_should_keep_player_balance_when_player_balance_when_location_already_have_a_owner(
        self,
    ):
        player2 = Player(behaviour=self.behaviour, balance=300)
        location = Location(cost_of_sale=150, cost_of_rent=55)
        location.owner = player2
        self.player.buy(location)
        expected = 300
        result = self.player.balance


class TestRandomBehaviour(TestCase):
    def setUp(self):
        self.behaviour = Random()
        self.player = Player(behaviour=self.behaviour, balance=300)

    @mock.patch("monopoly.behaviour.choice", return_value=True)
    def test_random_behaviour_buy_should_update_player_balance_when_random_value_is_true(
        self, mocked_choice
    ):
        location = Location(cost_of_sale=150, cost_of_rent=49)
        self.player.buy(location)
        expected = 150
        result = self.player.balance
        self.assertEqual(expected, result)

    @mock.patch("monopoly.behaviour.choice", return_value=False)
    def test_random_behaviour_buy_should_keep_player_balance_unchanged_when_random_value_is_false(
        self, mocked_choice
    ):
        location = Location(cost_of_sale=150, cost_of_rent=49)
        self.player.buy(location)
        expected = 300
        result = self.player.balance
        self.assertEqual(expected, result)


class TestCautiousBehaviour(TestCase):
    def setUp(self):
        self.behaviour = Cautious()
        self.player = Player(behaviour=self.behaviour, balance=300)

    def test_cautious_behaviour_should_keep_balance_unchanged_when_player_balance_less_location_cost_of_sale_result_lesser_than_80(
        self,
    ):
        location = Location(cost_of_sale=250, cost_of_rent=49)
        self.player.buy(location)
        expected = 300
        result = self.player.balance
        self.assertEqual(expected, result)

    def test_cautious_behaviour_repr_should_return_Cautious(self):
        expected = "Cautious"
        result = repr(self.behaviour)
        self.assertEqual(expected, result, "message")
