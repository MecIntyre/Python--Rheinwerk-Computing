namensliste = [
    "stephan",
    "mathias",
    "christian",
    "dyea",
    "norbert",
    "hubertus",
    ]

# Beispiel 1
# Anzeige der Namen die nicht auf "n" oder "s" enden.

gefilterteNamen = []
for name in namensliste:
    if not (name[-1] == "n") or (name[-1] == "s"):
        print(name)
        gefilterteNamen.append(name)
    
print()

# Beispiel 2
# List Comprehension (Vereinfachung der Darstellung)
# Anzeige der Namen die auf "n" oder "s" enden
gefilterteNamen = [name for name in namensliste if name[-1] in "sn"]


# Beispiel 3
# Amzeige der Namen die mit einem "s" anfange u
# und ein "a" als vorletzten Buchstaben haben.

for name in namensliste:
    if name[0] == "s" and name[-2] == "a":
        print(name)