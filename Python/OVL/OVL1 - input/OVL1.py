naam= input("Gelieve Uw naam in te voeren:")
leeftijd= input("Hartelijk dank, gelieve nu uw leeftijd in te voeren:")
if int(leeftijd) >= 18 and int(leeftijd) <= 50:
    print(f"Welkom {naam}.")
else: 
    print("Acces denied - Error 403")