# Schreiben Sie ein Programm zur Eingabe und Umrechnung von beliebigen
# Inch-Werten in Zentimeter.

# Umrechnungsfaktor
inch = 2.54

# Eingabe des Inch-Werts
print("Bitte geben Sie den Inch-Wert ein:")
xi = float(input())

# Umrechnung
xcm = xi * inch

# Ausgabe
print(xi, "Inch sind", xcm, "cm")