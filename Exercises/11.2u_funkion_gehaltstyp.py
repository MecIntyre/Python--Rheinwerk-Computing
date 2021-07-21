# wenn das Gehalt höchstens 450 beträgt, gibt die Zeichenkette Minijobber zurück
# ansonsten Normalverdiener.

def gehaltstyp(gehalt):
    if gehalt <= 450:
        return "Minijobber"
    else:
        return "Normalverdiener"

gehalt = int(input("Bitte gib dein Gehalt zur Bewertung ein: "))
print(gehaltstyp(gehalt))