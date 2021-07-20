essensListe = ["Döner", "Pizza", "Tortillas", "Lammrücken", "Nudelpfanne",]

for element in essensListe:
    print(element)

for essensIndex in range(0, 5, 1):   #range(startwert, endwert, Schrittweite)
    print(essensListe[essensIndex])