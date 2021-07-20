# Nutzer soll eine Zahl zwischen 1 und 10 eingeben
# Gib für die eingegebene Zahl alle Produkte zeilenweise aus.
# Z.B.: zahl * 1, zahl *2, ... , zahl * 10

# Lösung 1
produktListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

zahl = int(input("Bitte gib eine Zahl zwischen 1 und 10 ein: "))

for zahlIndex in range (0, 10, 1):
    print(produktListe[zahlIndex] * zahl)


# Lösung 2
zahl = int(input("Bitte gib eine Zahl zwischen 1 und 10 ein: "))

for faktor in range (1, 11):
    produkt = zahl * faktor
    print(faktor, ":", produkt)