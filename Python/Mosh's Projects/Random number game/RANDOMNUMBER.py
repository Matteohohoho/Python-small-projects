import random

def number_guessing_game():
    print("Choose the minimum and maximum numbers.")
    x = int(input("Minimum:"))
    y = int(input("Maximum:"))
    z = int(input("Maximus guesses:"))
    number = random.randint(x, y)
    guess = int(input(f"Guess a number from {x} to {y}! "))
    amount = 1

    while guess != number:
        if guess > number:
            lower_number()
            amount += 1
        else:
            higher_number()
            amount += 1

        guess = int(input("Try again! "))

    if amount > z:
        print(f"You reached your maximum guesses; the right number was {number}")

    print(f"Congratulations! You guessed the number in {amount} attempts.")

def lower_number():
    print("The number is lower than your guess.")

def higher_number():
    print("The number is higher than your guess.")

number_guessing_game()
