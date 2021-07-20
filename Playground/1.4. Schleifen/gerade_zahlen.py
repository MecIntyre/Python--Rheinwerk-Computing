# Gewünscht ist die Anzeige von geraden Zahlen

n = 10

while n >= 0:
    rest = n % 2
    if rest == 0:
        print("Die gerade Zahl ist", n)
    n -=1