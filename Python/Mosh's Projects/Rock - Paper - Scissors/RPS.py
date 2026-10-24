import random
# rock = 1, paper = 2, scissors = 3
def rock_paper_scissors():
    print("Welcome to rock, paper scissors.")
    choice = input("Rock, paper or scissors (r/p/s)? ")
    number = random.randint(0, 3)
    if choice == "r":
        choice = 1
    elif choice == "p":
        choice = 2
    else:
        choice = 3

    if choice == number:
        redo = input("You tied! Want to try again (Y/N): ")
        if redo.upper() == "Y":
            rock_paper_scissors()
        else:
            exit("Good Game")

    elif choice == 1 and number == 2:
        redo = input("You lost! Want to try again (Y/N): ")
        if redo.upper() == "Y":
            rock_paper_scissors()
        else:
            exit("Good Game")
    elif choice == 2 and number == 3:
        redo = input("You lost! Want to try again (Y/N): ")
        if redo.upper() == "Y":
            rock_paper_scissors()
        else:
            exit("Good Game")

    elif choice == 3 and number == 1:
        redo = input("You lost! Want to try again (Y/N): ")
        if redo.upper() == "Y":
            rock_paper_scissors()
        else:
            exit("Good Game")

    else:
        print("YOU WON!!!!!")
        
    

