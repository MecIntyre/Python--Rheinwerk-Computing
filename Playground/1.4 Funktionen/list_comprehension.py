namen = ["hans", "herbert", "rosi", "norbert", "hubertus"]

# Beispiel 1: Filterung nach Buchstabe h
namenMitAnfangsbuchstabenH = []
for name in namen:
    if name[0] == "h":
        #namenMitAnfangsbuchstaben = namenMitANfangsbuchstabenH + [name]
        namenMitAnfangsbuchstabenH.append(name)

print(namenMitAnfangsbuchstabenH)

# Vereinfachung --------> [name for name in namen if name[0] == "h"]


# Beispiel 2
def berechneQuadrat(zahl):
    quadrat = zahl * zahl
    return quadrat

zahlen = [1,2,3,4]
quadrate = map(berechneQuadrat, zahlen)
print(list(quadrate))