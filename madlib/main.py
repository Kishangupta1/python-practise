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


def computer_guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        # print(guess)
        feedback = input(f"Is {guess}, l or h or c\n").lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1

    print(f"comp guess correct: {guess}")


# guess_number(10)
computer_guess(20)