# Gegeben ist eine Zahl n >= 0
# Berechne die Summe s = 0 + 1 + 2 + ... + n-1 + n
# Formel: summe = n * (n + 1) / 2
# Beispiel: n = 7 s = 1+2+3+4+5+6+7 = 28

zahl = int(input("Bitte gib eine Zahl ein: "))
summe = 0

for summand in range (0, zahl + 1):
    summe = summand + summe
    print("Teilsumme:", summe)

print("Gesamtsumme:", summe)