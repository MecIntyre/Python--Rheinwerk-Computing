# Erzeuge eine neue Liste aus namen, 
# wobei die Elemente den Längen der einzelnen Namen entsprechen
#map, len, print, list

namen = [
    "hans",     #4
    "herbert",  #7
    "rosi",     #4
    "norbert",  #7
    "hubertus"  #8
]

print(list(map(len, namen)))
