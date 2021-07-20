umsatz = int(input("Gib den Umsatz ein:"))
provision = 0

if umsatz > 1_000_000:
    provision = umsatz * 0.2
elif umsatz > 500_000:
    provision = umsatz + 0.1
elif umsatz > 100_000:
    provision = umsatz * 0.05
else:
    provision = 0

print("Ihre Provision:", provision)