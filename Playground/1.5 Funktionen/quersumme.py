# Berechnung der Quersumme 

def berechneQuersumme(zahl):
    quersumme = 0
    zeichenkette = str(zahl)
    for einZeichen in zeichenkette:
        ziffer = int(einZeichen)
        quersumme = quersumme + ziffer
    return quersumme


zahl = int(input("Bitte gib eine Zahl zur Berechnung der Quersumme ein: "))
print(berechneQuersumme(zahl))


        