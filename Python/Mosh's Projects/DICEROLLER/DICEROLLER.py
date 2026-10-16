import random

def dobbelen():
    dobbelsteen1 = random.randint(1,6)
    dobbelsteen2 = random.randint(1,6)
    print (f"({dobbelsteen1}, {dobbelsteen2})")

    again = input("Wilt u opnieuw dobbelen? (y/n):")

    if again == "y":
        dobbelen()
    else:
        print("OK")

dobbelen()