from os import stat

# Öffnen einer Textdatei mit UTF8-Kodierung
# Aufhebung (mit r) von Sonderfunktionen der Zeichen, z.b. Slash
data = open(r'Utils/rfc2929.txt', encoding='utf-8')

# alle Zeilen aus Datei lesen und in Variable zeilen speichern
# Datei wieder schließen und für weitere Zugriffe freigeben
content = data.read() 
data.close() 

# Sortierfunktion zur paarweisen Sortierung der Groß- und Kleinbchstaben.
# Hole wert des Schlüssels und verlgeiche anhand des Wertes.
def sortLogic(characters):
    return characters.lower()

# statistic = Dictionary = {'a': 10, 'c': 5, 'amountWords': 40}
# Auflistung der alphanumerischen Zeichen aus der RFC-Textdatei
statistic = {}
for characters in content:
    if not characters.isalnum():
        continue
    if characters in statistic:
        statistic[characters] += 1
    else:
        statistic[characters] = 1

# Sortierungsvariante 1: Alphabetische Sortierung mit Hilfe der eigenen Sortier-Funktion:
sortedKeys = sorted(statistic, key=sortLogic)
for characters in sortedKeys:
    print("Zeichen:", characters, "Anzahl", statistic[characters])

# Sortierungsvariante 2, absteigend, numerische Sortierung nach höchstem Wert:
sortedKeys = sorted(statistic, key=lambda z: statistic[z])
sortedKeys.reverse()
for characters in sortedKeys:
    print("Zeichen:", characters, "Anzahl", statistic[characters])
