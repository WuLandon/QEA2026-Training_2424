import random


def guessing_game():
    answer = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        guess = int(input("guess number from 1 to 100: "))

        if guess == answer:
            return "congrats"
        if guess < answer:
            print("too low")
        else:
            print("too high")

        attempts -= 1

    return f"Ran out of attempts. Answer was {answer}"


print(guessing_game())
