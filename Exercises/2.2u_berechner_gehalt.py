# Lass dir das Gehalt vom Nutzer eingeben.
# Wenn das Gehalt kleiner gleich 450€ ist, dann gib "Minijobber" aus.
# Wenn 450 < gehalt <= 1000€, dann gib "Billiglohnarbeiter" aus.
# Wenn 1000 < gehalt <= 2000€, dann "Normalverdiener" ausgeben.
# Wenn gehalt > 8000€ gib "Spitzenverdiener" aus.
# Teste mit den Werten: 300, 450, 1000, 1500, 3000 und 9000

gehalt = int(input("Bitte gib dein Gehalt ein: "))

if gehalt <= 450:
    print("Haha Minijobber!")
elif gehalt <= 1000:
    print("Billiglohnarbeiter!")
elif gehalt <= 2000:
    print("Normalverdiener!")
elif gehalt > 8000:
    print("Prollender Spitzenverdiener!")
elif 2000 < gehalt <= 8000 > 1000:
    print("Normalverdiener!")
else: 
    print("Keine Ahnung!")