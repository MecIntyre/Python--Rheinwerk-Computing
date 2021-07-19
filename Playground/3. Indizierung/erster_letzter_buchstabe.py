eingabe = input("Zeichenkette eingeben:")
eingabeGroß = 4* eingabe.upper()
print("Vierfache Eingabe in groß", eingabeGroß)


if len(eingabe) >= 2:
    print(eingabe[0], eingabe[1], eingabe[-2], eingabe[-1])
else:
    print("Eingabe zu kurz!")
