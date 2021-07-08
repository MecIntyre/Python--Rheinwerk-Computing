# Schreiben Sie ein Programm, das die folgende Ausgabe erzeugt.
# 15 Inch = 38.1cm, 20 Inch = 50.8cm, 25 Inch = 63.5cm, 
# 30 Inch = 76.2cm, 35 Inch = 88.9cm, 40 Inch = 101.6cm

# Umrechnungsfaktor
inch = 2.54

# Schleife
for xi in range (15, 41, 5):
    xcm = xi * inch
    print(xi, "Inch =", xcm, "cm")