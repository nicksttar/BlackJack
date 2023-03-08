import random
import os
import time


class Deck:
    """Class to make someting with deck"""

    def __init__(self) -> None:
        HEARTS = chr(9829) # ♥
        DIAMONDS = chr(9830) # ♦
        SPADES = chr(9824) # ♠
        CLUBS = chr(9827) # ♣
        self.masty = [HEARTS, DIAMONDS, SPADES, CLUBS]

    def get_deck(self) -> list:
        """Creates deck to each round"""
        c = ["V", "Q", "K", "T"]
        val_deck = [j+i for i in self.masty for j in c]
        num_deck = [str(j)+i for i in self.masty for j in range(2,11)]
        full_deck = num_deck+val_deck
        return full_deck

    def get_card(self, deck: list) -> str:
        """Returns random card and remove it from deck till end game"""
        card = random.choice(deck)
        deck.remove(card)
        return card

    def get_cards_dict(self) -> dict:
        """Dictionary with value of each cards"""
        dict = {}
        deck = self.get_deck()
        for i in deck:
            if i[0:-1].isdigit():
                dict[i] = int(i[0:-1])
            elif i[0:-1].isalpha() is True:
                dict[i] = int({"V": 10, "Q": 10, "K": 10, "T": 11}[i[0:-1]])
        return dict

    def get_cards_value(self, card: str) -> int:
        """Function which gets card value"""
        new_card = card
        dict = self.get_cards_dict()
        return dict[new_card]


class User:
    """User settings"""
    def __init__(self, name, money=5000) -> None:
        self.name = name
        self.money = money

    def geet_user(self) -> print:
        time.sleep(1)
        return print("""
Rules of the Black Jack:
Before the game you place a bet and the game starts. There is a deck of cards with values ​​from 2 to 21. 
At the beginning of each round you have two cards your task is to make the number of points more than your opponent, 
but not more than 21 otherwise there will be a bust. You can take 1 card or leave your points as they are. 
The opponent draws an additional card until he has 18 points or more. At the end of the game, 
if you have 21 or less points but more than your opponent, you get a win depending on your bet.
P.S: write c to command""")

    def geet_new_user(self) -> print:
        return print("You are a new user!!! We saved you")


class Game:
    """Game settings"""
    def __init__(self) -> None:
        self.enemy_cards = []
        self.b = 0
        self.your_cards = []
        self.a = 0

    def inroduction(self) -> print:
        return print("""----------------------------
Black Jack by nicksttar v1.0
----------------------------
""")

    def _clear_data(self, files: list=["dashboard.txt", "users.txt"]) -> None:
        """Cleaner data files"""
        for i in files:
            time.sleep(1)
            print("\nCache was cleared")
            os.remove(i)
