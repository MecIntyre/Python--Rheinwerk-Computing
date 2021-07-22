# Schreiben Sie das Programm aus Übung 11u_parameter um.
# Die Steuer soll innerhalb der Funktion steuer() berechnet und an das Hauptprogramm zurückgeliefert werde.
# Die Ausgabe des Werts soll im Hauptprogramm stattfinden.

# Funktion
def steuer(gehalt):
    # Umrechnung
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18
    
    # Ergebnis senden
    return steuerbetrag

# Verschiedene Werte
print("Gehalt: 1800€, Steuer:", steuer(1800), "Euro")
print("Gehalt: 2200€, Steuer:", steuer(2200), "Euro")
print("Gehalt: 2500€, Steuer:", steuer(2500), "Euro")
print("Gehalt: 2900€, Steuer:", steuer(2900), "Euro")
