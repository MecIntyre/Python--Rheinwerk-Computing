# Zufallsgenerator
import random
random.seed()

# Werte und Berechnung 
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print ("Die Aufgabe:", a, "+", b)

# Schleife und Anzahl initialisieren
zahl = c + 1
versuch = 0

# while-Schleife
while zahl != c:
    # Anzahl Versuche
    versuch = versuch + 1

    # Eingabe
    print("Bitte eine Zahl eingeben:")
    z = input()

    # Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        # Falls Umwandlung nicht erfolgreich
        print("Sie haben keine ganze Zahl eingegeben")
        # Schleife unmittelbar fortsetzbar
        continue

    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        # Abbruch der Schleife
        break
    else:
        print(zahl, "ist falsch:")

# Anzahl ausgeben 
print("Ergebnis:", c)
print("Anzahl Versuche:", versuch)
