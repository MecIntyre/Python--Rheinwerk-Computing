# Das vereinfachte Programm zur Berechnung der Steuer wird verändert.
# Der Anwender wird dazu aufgefordert, sein monatliches Gehalt einzugeben.
# Liegt es über 2500 Euro, sind 22% Steuern zu zahlen, ansonsten 18%.

# Eingabe
print("Geben Sie ihr Gehalt in Euro ein:")
gehalt = float(input())

# Umrechnung
if gehalt > 2500:
    steuerbetrag = gehalt * 0.22
else:
    steuerbetrag = gehalt * 0.18

# Ausgabe
print("Es ergibt sich eine Steuer von", steuerbetrag, "Euro")