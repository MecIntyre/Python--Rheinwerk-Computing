namen = [
    "stephan",
    "mathias",
    "christian",
    "dyea",
    "norbert",
    "hubertus",
    ]

# Beispiel 1
# Anzeige der Namen die auf "n" und "s" enden.

for name in namen:
    if (name[-1] == "n") or (name[-1] == "s"):
        print(name)
    #if name[-1] == "s":
    #    print(name)

print()

# Beispiel 2
# Amzeige der Namen die mit einem "s" anfange u
# und ein "a" als vorletzten Buchstaben haben.

for name in namen:
    if name[0] == "s" and name[-2] == "a":
        print(name)