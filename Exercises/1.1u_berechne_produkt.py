# Lasse dir zwei Zahlen vom Benutzer geben und berechne das Produkt.
# Wenn das Produkt größer als 100 ist, gib stattdessen die Summe der beiden Zahlen aus.

eingabe1 = input("Zahl1:")
eingabe2 = input("Zahl2:")

zahl1 = int(eingabe1)
zahl2 = int(eingabe2)

produkt = zahl1 * zahl2

if produkt > 100:
    summe = zahl1 + zahl2
    print("Summe:", summe)
else:
    print("Produkt:", produkt)
