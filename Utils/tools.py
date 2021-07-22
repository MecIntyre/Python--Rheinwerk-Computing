import json

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

# Einbinden der externen JSON-Datei (Fragenliste)
def loadQuestionList(path):
    questionData = open(path, encoding="utf-8")
    questionList = json.load(questionData)
    questionData.close()
    return questionList


# Aufruf der Funktion zur Einbindung der JSON-Datei
questionList = loadQuestionList(r"Playground\fragen.json")
