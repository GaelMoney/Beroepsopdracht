print ("Hello You!")
print ("Ik ben Gael Griffith")
print ("wie ben jij?")
print ("typ je naam in: ")

inputnaam = input()

print ("Hallo " + inputnaam) 
print ("Welke kledingmerk vindt ik het leukst?")
print ("A. Smib")

print ("B. Stuzzy")

print ("C. Daily paper")

antwoord = input("typ A, B of C: ")
 
if antwoord == "A" or antwoord =="a":

     print (" jouw antwoord was: " + antwoord + ", " + " dit is goed")

if antwoord == "B" or antwoord =="b":

     print ("nee dat klopt niet ik hou er wel van")

if antwoord == "C" or antwoord =="c":

     print ("nee")

else:

     print (" je kunt alleen mat A, B of C antwoorden")
