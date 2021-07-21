# Es soll wiederum die Steuer für verschiedene Gehälter berechnet werden.
# Liegt das Gehalt über 2500€, sind 22% Steuern zu zahlen, ansonsten 18%.
# Die Berechnung und die Ausgabe der Steuer sollen diesmal innerhalb einer Funktion mit dem Namen steuer() stattfinden.
# Die Funktion soll für die folgenden Gehälter aufgerufen werden: 1800€, 2200€, 2500€ und 2900€

# Funktion
def steuer(gehalt):
    # Umrechnung
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18

    # Ausgabe
    print("Gehalt:", gehalt, "Euro, Steuer:", steuerbetrag, "Euro")

    # Verschiedne Werte
    steuer(1800)
    steuer(2200)
    steuer(2500)
    steuer(2900)
