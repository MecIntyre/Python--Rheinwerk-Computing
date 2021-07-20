# Schreiben Sie ein Programm zur vereinfachten Berechnung der Steuer
# Der Anwender wird dazu aufgefordert, sein monatliches Gehalt einzugeben.
# Anschließend werden 18% dieses Beitrags berechnet und ausgegeben.

# Eingabe
print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())

# Umrechnung
steuerbetrag = gehalt * 0.18

# Ausgabe
print("Es ergibt sich eine Steuer von:", steuerbetrag, "Euro")