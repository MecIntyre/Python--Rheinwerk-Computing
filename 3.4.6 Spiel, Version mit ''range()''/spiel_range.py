# Modul random importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Werte und Berechnung 
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print ("Die Aufgabe:", a, "+", b)

# for-Schleife mit range
for versuch in range(1,10):
    # Eingabe
    print("Bitte eine Zahl eingeben:")
    z = input()
    zahl = int(z)

    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        # Abbruch der Schleife
        break
    else:
        print(zahl, "ist falsch:")

# Ergebnis + Anzahl
print("Ergebnis:", c)
print("Anzahl Versuche:", versuch)