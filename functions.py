from time import sleep
from sys import exit


def exit_func() -> None:
    """Function which make system exit"""
    print("See you soon!")
    sleep(1)
    exit()


def validator(question: str) -> str or None:
    """Basic anty-dump validator"""
    user_input = input(question)
    while user_input not in ["y", "n", "q"]:
        user_input = input(question)
    if user_input == "y":
        return "y"
    elif user_input == "n":
        return "n"
    elif user_input == "q":
        exit_func()


def bet_validator(question: str, amount_money: int) -> int:
    """Bet anty-dump validator"""
    user_input = input(question)
    while user_input.isdigit() != True or int(user_input) > amount_money:
        print("Bet number less or equal than you have!")
        if user_input == "q":
            exit_func()
        user_input = input(question)
    return int(user_input)


def dashboard(dashboard_data: str) -> print:
    """Function which show dashboard if it avaliable"""
    try:
        with open(dashboard_data) as f:
            file2 = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("There is no scores right now")
    else:
        results_t = []
        for word in file2:
            temp = word.split("-")
            results_t.append([temp[0].strip(), int(temp[1].strip())])
        results = sorted(results_t, key=lambda x:x[1], reverse=True)
        for ind, num in enumerate(results, 1):
            print(f"{ind}.", " - ".join([str(n) for n in num]))


def results(user_cash: str, enemy_cash: str, bet: int) -> int:
    """Function which counts results of each black jack round"""
    if user_cash > enemy_cash and user_cash <= 21:
        return bet 
    elif user_cash > enemy_cash and user_cash > 21:
        return -bet
    elif user_cash < enemy_cash and enemy_cash <= 21:
        return -bet
    elif user_cash < enemy_cash and enemy_cash > 21 and user_cash <=21:
        return bet
    elif user_cash < enemy_cash and enemy_cash > 21 and user_cash > 21:
        return -bet
    elif user_cash == enemy_cash:
        return 0
    elif user_cash > 21 and enemy_cash > 21:
        return 0
    

def show_scores():
    user_input = validator("Show scores? y/n: ")
    if user_input == "y":
        return dashboard("dashboard.txt")

def show_cards(your_c, enemy_c, result="one"):
        for card_u in your_c:
            print(card_u, end=" ")
        print("\n")
        for card_e in enemy_c:
            print(card_e, end=" ")
        print("\n")

        if result=="one":
            return card_e
        elif result=="two":
            return [card_u, card_e]
        