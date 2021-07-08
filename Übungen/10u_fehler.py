# Verbessern Sie das Programm zur Eingabe und Umrechnung eines beliebigen Inch-Wertes in Zentimeter.
# Eingabefehler des Anwenders sollen abgefangen werden.
# Das Programm soll den Anwender so lange zur Eingabe auffordern, bis sie erfolgreich war.

# Umrechnungsfaktor
inch = 2.54

# Initialisierung der while-Schleife
fehler = 1

# Schleife bei falscher Eingabe
while fehler == 1:
    # Eingabe
    print("Bitte geben Sie den Inch-Wert ein")
    xi = input()

    # Versuch der Umwandlung
    try: 
        xi = float(xi)
        fehler = 0
    # Fehler bei Umwandlung
    except:
        print("Falsche Eingabe")

# Umrechnung, Ausgabe
xcm = xi * inch
print (xi, "Inch sind", xcm, "cm")