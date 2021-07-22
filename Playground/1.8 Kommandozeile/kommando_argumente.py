import sys

for argument in sys.argv:
    print(argument)

if "--help" in sys.argv:
    print("Ich habe keine Dokumentation")