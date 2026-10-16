import random

def computer_choice():
    global number
    number = random.int(1,3)

def rock_paper_scissors():
    print("Welcome to rock, paper scissors.")
    choice = input("Rock, paper or scissors? (r/p/s)")
    computer_choice()
    r = 1
    p = 2
    s = 3
    if choice == number:
        again = input("You tied, try again?")
        rock_paper_scissors()
    elif choice == 1 and number == 2:
        again = input("You won, try again?")
        rock_paper_scissors()
    elif choice == 1 and number == 3:
        again = input("You lost, try again?")
        rock_paper_scissors()
    elif choice == 2 and number == 1:
        again = input("You won, try again?")
        rock_paper_scissors()
    elif choice == 2 and number == 3:
        again = input("You lost, try again?")
        rock_paper_scissors()
    elif choice == 3 and number == 1:
        again = input("You lost, try again?")
        rock_paper_scissors()
    elif choice == 3 and number == 2:
        again = input("You won, try again?")
        rock_paper_scissors()

