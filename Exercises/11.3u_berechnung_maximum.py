# Berechnung des Maximumwertes
# nur mit Vergleichsoperatoren

def berechneMaximum(x, y, z):
    if x < y:
        # x kann definitiv nicht das Maximum sein
        if y < z:
            return z
        else:
            return y
    else: 
        if x < z:
            return z
        else:
            return x
    
x = int(input("Bitte gib die erste Zahl ein: "))
y = int(input("Bitte gib die zweite Zahl ein: "))
z = int(input("Bitte gib die dritte Zahl ein: "))
print(berechneMaximum(x, y, z))