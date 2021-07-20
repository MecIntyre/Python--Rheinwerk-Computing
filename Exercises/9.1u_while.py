# Schreiben Sie ein Programm, das den Anwender wiederholt dazu auffordert, einen Wert in Inch einzugeben
# Der eingegebene Wert soll anschließend in Zentimeter umgerechnet und ausgegeben werden.
# Das Programm soll nach der Eingabe 0 beendet werden.

# Umrechnungsfaktor
inch = 2.54

# Erste Eingabe
print("Bitte geben Sie den Inch-Wert ein:")
xi = float(input())

# while-Schleife
while xi != 0:
    # Umrechnung, Ausgabe
    xcm = xi * inch
    print(xi, "Inch sind", xcm, "cm")

    # Weitere Eingabe
    print("Bitte geben Sie den Inch-Wert ein:")
    xi = float(input())
