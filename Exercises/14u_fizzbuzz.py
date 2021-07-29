# Schreibe ein Programm, dass die Zahlen von 1 bis 100 durchläuft:
# ist die Zahl durch 3 teilbar, gibt das Programm "Fizz" aus
# ist die Zahl durch 5 teilbar, gibt das Programm "Buzz" aus
# ist die Zahl durch 3 und 5 teilbar, gibt das Programm "FizzBuzz" aus
# andernfalls wird die Zahl ausgegeben

input = int(input("Bitte gib eine Zahl von 1 bis 100 ein: "))

for input in range(1,101):
    if input % 3 == 0 and input % 5== 0:
        print ("FizzBuzz")
    elif input % 3 == 0:
        print ("Fizz")
    elif input % 5 == 0:
        print ("Buzz")
    else:
        print (input)