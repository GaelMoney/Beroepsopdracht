import time
print("wat is jouw naam?")
inputnaam = input()

def deel0():
    print ("Dit is een keuze verhaal")
    time.sleep(1.5)
    print ("Dit verhaal heeft 4 verschillende eindes")
    time.sleep(2)
    print ("Je hebt maar 1 goed einde dus good luck on your journey")
    deel1()
    

def deel1():
    print ("Hallo " + inputnaam)
    time.sleep(2)
    print ("Jij bevindt je nu in ...")
    time.sleep(2)
    print ("Vorige week heb jij een afspraak gemaakt met een verdachte man om naar Nederland te komen")
    time.sleep(2)
    print ("De verdachte man zou jouw vandaag om 8 uur in de avond ophalen")
    time.sleep(2)
    print ("Het enigste probleem is... het is nu 10 over 8 en er is nog steeds niemand gekomen")
    time.sleep(2)
    print (inputnaam + " ...")

    while True:
        antwoord = input("Maak een keuze, A of B?")
        if antwoord == "A":
            deel2()
            break
        elif antwoord == "B":
            deel3()
            break
        else:
            print("Je kunt alleen antwoorden met A of B.")
            deel1()

def deel2()


































































deel0()

