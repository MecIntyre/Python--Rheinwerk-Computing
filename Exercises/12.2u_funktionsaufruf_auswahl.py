# Gib folgende Optionen aus: ja, nein, vielleicht
# Lese Eingabe mit folgenden Werten: j, n, v

def readInput(prompt, inputChoice):
    while True:
        choice = input(prompt)
        choice = choice.lower()
        if choice in inputChoice:
            return choice

# Ausgabe einer Liste der Auswahlmöglichkeiten.
def showChoice(choiceOptions):
    print("Das ist die Auswahl:")
    for index, option in enumerate(choiceOptions):
        print(index + 1, ": ", option, sep="")

showChoice(["ja", "nein", "vielleicht"])
readInput("Mögliche Eingabe: (j, n, v): ", ["j", "n", "v"])