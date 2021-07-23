import Utils.tools
import random

# Import der Wortliste und Initalisierung der Funktion
# Filter nach Substantive durch Großbuchstabenerkennung
# Umwandeln in Kleinbuchstaben und entfernen des Whitespaces
def loadWordList(path):
    wordlist = []
    data = open(path, encoding='utf-8')
    for line in data:
        line = line.strip()
        if line[0].isupper():
            wordlist.append(line.lower())
    data.close()
    return wordlist

# Aufruf der Wordlist-Funktion
# Initialisierung des Lösungswortes durch Zufallsgenerator
# Lösungswort ohne duplizierte Buchstaben.
wordlist = loadWordList(r"Utils/wordlist.txt")
randomIndex = int(random.uniform(0, len(wordlist)))
solution = wordlist[randomIndex]
solutionOnly = set(solution)

# Darstellung des verdeckten Lösungswortes und der Unterstriche.
def reveal(word, characterList):
    for character in word:
        if character in characterList:
            print(character, " ", end="")
        else:
            print("_ ", end="")

# Anlegen eines Sets mit einer Eingabebegrenzung auf A bis Z und Umlaute.
# Versuchszähler auf 0 gesetzt.
inputCharacters = set()
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['ö', 'ü', 'ä', 'ß']
trials = 0

# Dauerschleife zum Anzeigen der eingegebenen und Hilfsbuchstaben.
# Import der readInput-Funktion aus Utils.tools
while True:
    reveal(solution, inputCharacters)
    print()
    input = Utils.tools.readInput("Buchstabe eingeben: ", letters)
    
    # Prüfung nach doppelter Eingabe und Rückmeldung
    if input in inputCharacters:
        print("Doppelte Eingabe ist unzulässig!")
        trials += 1
        continue
    inputCharacters.add(input)

    # Prüfung nach richtiger Eingabe und Rückmeldung
    if input in solution:
        print("Richtig geraten!")
    
    # Rückmeldung nach falscher Eingabe
    # Abbruch falls das Lösungswort erraten wird.
    else: 
        print("Leider falsch geraten!")
    trials += 1
    if inputCharacters.issuperset(solutionOnly):
        break

print(f"Du hast das Lösungswort {solution} nach {trials} Versuchen erraten!")