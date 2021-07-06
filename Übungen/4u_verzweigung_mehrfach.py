# Das Programm zur Berechnung der Steuer wird weiter verändert.
# Der Anwender wird dazu aufgefordert, sein monatliches Gehalt einzugeben.
# Anschließend wird seine Steuer nach folgenden Kriterien berechnet: 
# mehr als 4000€, 26% Steuern, 2500€ bis 4000€ sind es 22% Steuern und weniger als 2500€ sind es 18% Steuern.

# Eingabe
print("Geben Sie ihr Gehalt in Euro ein:")
gehalt = float(input())

# Umrechnung
if gehalt > 4000:
    steuerbetrag = gehalt * 0.22
elif gehalt < 2500:
    steuerbetrag = gehalt * 0.18
else:
    steuerbetrag = gehalt * 0.22

# Ausgabe
print("Es ergibt sich eine Steuer von", steuerbetrag, "Euro")