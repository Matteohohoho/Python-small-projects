import json
import os

with open("data.json", "r") as bestand: #best om het iets zoals reviews.json te noemen, voor grote programmas --> veel JSON 
    reviews = json.load(bestand)


def review_tool():
    global reviews # met global reviews geef je aan dat je de variabele gebruikt die buiten de functie is aangemaakt, en niet een nieuwe lokale variabele.

    print("Welkom bij de reviewtool van Spotify!")

    naam = input("Gelieve uw naam in te voeren: ")
    nummer = input("Welk liedje wilt u reviewen? ")
    score = input("Geef een score op 10: ")
    link = input("Plak hier je link: ")

    reviews[naam] = {
        "naam": naam,
        "nummer": nummer,
        "score": score,
        "link": link
    }

    

    with open("data.json", "w") as bestand:
        json.dump(reviews, bestand, indent=4, ensure_ascii=False) # ensure_ascii=False toegevoegd om speciale tekens correct weer te geven in json

    redo_or_not = input(
        "Wilt u nog een liedje reviewen? "
        "Typ 'ja' of 'nee'. "
        "Wilt u uw reviews bekijken? Typ 'bekijk': "
    ).lower() #zet de input om naar kleine letters

    if redo_or_not == "ja":
        review_tool() # altijd haakjes na functie anders word de functie niet uitgevoerd

    elif redo_or_not == "nee":
        print("Bedankt voor de review!")

    elif redo_or_not == "bekijk":
        print(json.dumps(reviews, indent=4, ensure_ascii=False)) #indent=4 toegevoegd voor betere leesbaarheid van de output (inspringingen)

    else:
        input("Ongeldige keuze. Wilt u nog een liedje reviewen? Typ 'ja' of 'nee'. Wilt u uw reviews bekijken? Typ 'bekijk': ")


review_tool() # door de functie onderaan te scrijven word de functie gebruit bij het opstarten van het programma