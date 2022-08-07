import random


def guess_number(num):
    random_num = random.randint(1, num)
    guess = 0
    while guess != random_num:
        guess = int(input("guess the no:"))
        if guess < random_num:
            print("you are low.")
        elif guess > random_num:
            print("you are high")
    print(f"you guessed:{guess} and correct no. {random_num}")


guess_number(10)
