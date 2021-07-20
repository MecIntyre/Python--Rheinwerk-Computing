
import random

print("Das sind die folgenden Möglichkeiten:")
print("")

essensListe = [
    "Döner",
    "Pizza",
    "Tortillas",
    "Lammrücken",
    "Nudelpfanne",]

index = 0
while index <= 4:
    print(essensListe[index])
    index += 1

print("")
index = int(random.uniform(0, len(essensListe)))
print("Du isst heute", essensListe[index],"!")
