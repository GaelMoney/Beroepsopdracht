import time

print ("Dit is een keuze verhaal")
time.sleep(1.5)
print ("Dit verhaal heeft 4 verschillende eindes")
time.sleep(2)
print ("Je hebt maar 1 goed einde dus good luck on your journey")
time.sleep(2)
print ("Voor dit verhaal zullen we jouw naam gebruiken dus vul die maar hierin: ")

inputnaam = input()

def Verhaalstukje1():
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

    antwoord = input("Maak een keuze, A of B?")
    if antwoord == "A":
        Verhaalstukje2()
    elif antwoord == "B":
        Verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        Verhaalstukje1()



