from bj_class import Deck, User, Game
from functions import validator, bet_validator, dashboard, results, exit_func, show_scores, show_cards


game = Game()
game.inroduction()
users_data = "users.txt"

def script():
    new_user = User(input("Write your name, dude: "))
    try:
        with open(users_data) as f:
            file1 = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        new_user.geet_new_user()
        with open(users_data, "w") as new_file:
            new_file.write(new_user.name + "\n")
    else:
        if new_user.name in file1:
            print("Wellcome back")
        elif new_user.name not in file1:
            with open(users_data, "a") as file:
                file.write(new_user.name + "\n")
                new_user.geet_new_user()

    user_input = validator("Show rules? y/n: ")
    if user_input == "y":
        new_user.geet_user()

    money = new_user.money

    deck = Deck()
    while True:

        enemy_cards, your_cards = [], []
        enemy_points, your_points = 0, 0
        new_deck = deck.get_deck()
        print(f"Cash balance is {money}\n")

        bet = bet_validator("Your bet: ", money)
        print(f"{new_user.name} is betting {bet}\n")

        while enemy_points <= 18 and your_points <= 21:
            
            enemy_cards.append(deck.get_card(new_deck))
            your_cards.append(deck.get_card(new_deck))
            
            res = show_cards(your_cards, enemy_cards, result="two")
            enemy_points += deck.get_cards_value(res[1])
            your_points += deck.get_cards_value(res[0])
            
            print(f"Your points: {your_points}", f"Enemy points: {enemy_points}", sep="\n")

            if enemy_points == 18 or enemy_points >= 21 or your_points >= 21:
                break
            
            user_input = validator("Take more? y/n: ")
            if user_input == "y":
                continue
            elif user_input == "n":
                if enemy_points <= 18:
                    while enemy_points <= 18:
                        enemy_cards.append(deck.get_card(new_deck))

                        res = show_cards(your_cards, enemy_cards, result="one")
                        enemy_points += deck.get_cards_value(res)
                
                        print(f"Your points: {your_points}", f"Enemy points: {enemy_points}", sep="\n")
                elif enemy_points >= 18:
                    break


        money += results(your_points, enemy_points, bet)
        print(f"Now you have {money}")


        user_input = validator("Countinue? y/n: ")
        if user_input == "n":
            user_input = validator("Save your score? y/n: ")
            if user_input == "y":
                dashboard_data = "dashboard.txt"
                try:
                    with open(dashboard_data) as f:
                        file2 = f.readlines()
                except FileNotFoundError:
                    print("\nYou are the first on this board dude)))")
                    print("Now you can see dashboard after next game1")
                    with open(dashboard_data, "w") as f:
                        f.write(f"{new_user.name} - {money}\n")
                        print("Data saved")
                else:
                    with open(dashboard_data, "a") as f:
                        f.write(f"{new_user.name} - {money}\n")
                        print("Data saved")
                        show_scores()
                        
                    user_input = validator("Do you want to clear game cache? y/n: ")
                    if user_input == "y":
                        game._clear_data()
                    elif user_input == "n":
                        exit_func()
            elif user_input == "n":
                show_scores()
        elif user_input == "y":
            continue


if __name__ == "__main__":
    script()
