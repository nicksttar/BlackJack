import unittest
from black_jack_oop import Deck, User

class UnitTest(unittest.TestCase):
    """Tests of working class Deck"""
    def setUp(self):
        self.create_deck = Deck()
        self.new_deck = self.create_deck.get_deck()
        self.full_deck = ['2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', '2♦', '3♦', '4♦', 
        '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', '2♣','3♣', '4♣', 
        '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'V♥', 'Q♥', 'K♥', 'T♥', 'V♦', 'Q♦', 'K♦', 'T♦', 'V♠', 'Q♠', 'K♠', 'T♠', 'V♣', 'Q♣', 'K♣', 'T♣']
        self.full_deck_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9,
         10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 10, 10, 10, 11, 10, 10, 10, 11, 10, 10, 10, 11]
        self.full_deck_dict = {'2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, '2♦': 2, '3♦': 3, '4♦': 4, 
        '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 
        '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'V♥': 10, 'Q♥': 10, 'K♥': 10, 'T♥': 11, 'V♦': 10, 'Q♦': 10, 
        'K♦': 10, 'T♦': 11, 'V♠': 10, 'Q♠': 10, 'K♠': 10, 'T♠': 11, 'V♣': 10, 'Q♣': 10, 'K♣': 10, 'T♣': 11}

        self.new_user = User("User")



    def test_get_deck(self):
        self.assertEqual(self.new_deck, self.full_deck)
        self.assertEqual(type(self.new_deck), type(self.full_deck))

    def test_get_card(self):
        for _ in range(52):
            self.assertIn(self.create_deck.get_card(self.new_deck), self.full_deck)

    def test_get_cards_dict(self):
        self.assertEqual(self.full_deck_dict, self.create_deck.get_cards_dict())

    def test_gets_cards_value(self):
        for ind in range(52):
            self.assertEqual(self.create_deck.get_cards_value(self.full_deck[ind]), self.full_deck_dict[self.full_deck[ind]])






if __name__ == "__main__":
    unittest.main()