# Lass den Nutzer solange eine Eingabe tätigen, 
# bis sie einer der vorgegebenen Möglichkeiten entspricht.
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

def calculateSumAndProduct(a, b):
    sum = a + b
    product = a * b
    return (sum, product)   # Ausgabe als tuple

x, y = calculateSumAndProduct(2, 4) # Speichern der Argumente des Tuples direkt in x und y
print(x, y)

showChoice(["Stephan", "Mathias", "Christian", "Dyea", "Norbert"])
readInput("Mögliche Eingabe: (1 - 5): ", ["1", "2", "3", "4", "5"])