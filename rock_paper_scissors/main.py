import random


def play():
    user_input = input("R/P/S\n").lower()
    computer = random.choice(['r', 'p', 's'])

    # r > s, s > p, p>s
    if user_input == computer:
        return print(f"draw")

    if is_win(user_input, computer):
        return print(f"you win!")

    return print(f"you lost!")


def is_win(player, opponent) -> bool:
    if any([player == 'r' and opponent == 's', player == 's' and opponent == 'p', player == 'p' and opponent == 's']):
        return True


play()