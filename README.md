# BlackJack
This is a simple command-line implementation of the popular casino game Blackjack, also known as 21.

## Installation
1. Clone the repository: git clone https://github.com/nicksttar/BlackJack.git
2. Navigate to the project directory: cd BlackJack
3. Run the game: python3 main.py
## How to Play
The game is played against the dealer. The goal is to get a hand value of 21 or as close to 21 as possible without going over. Face cards (Jacks, Queens, and Kings) are worth 10 points, Aces are worth 11 points, and all other cards are worth their face value.

At the beginning of the game, you and the dealer are dealt one cards each. You can see one of the dealer's cards and one of your cards. Based on the cards you see, you can choose to tke more and receive another card or Dont take more and keep your current hand. You can continue to take more until you either choose to stand or your hand value exceeds 21, in which case you "bust" and lose the game.

After you stand, the dealer will reveal their hidden card and hit until their hand value is 18 or greater. If the dealer busts, you win the game. If the dealer's hand is greater than or equal to yours and does not bust, you lose the game. If your hand is greater than the dealer's hand and neither of you busts, you win the game.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
