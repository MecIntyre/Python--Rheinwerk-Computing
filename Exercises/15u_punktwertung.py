# Bei internationalen Wettkämpfen bewerten in Einzelwettbewerben sieben Wettkampfrichter die Sprünge.
# Jeder vergibt pro Sprung 0 bis 10 Punkte, mit Schritten von halben Punkten.
# Die zwei höchsten und niedrigsten resulten werden gestrichen.
# Die verbleibenden drei resulten werden addiert und das Ergebnis mit dem Schwierigkeitsgrad multipliziert.
# Das Endresultat entspricht der erzielten Punktzahl des Springers.

# Beispiel 1:
# Schwierigkeitsgrad: 2,1
# Punkte: 7,5 | 7,5 | 7,0 | 8,0 | 8,0 | 7,5 | 8,5
# Gestrichen: 7,5 | 7,5 | 7,0 | 8,0 | 8,0 | 7,5 | 8,5
# result: 7,5 + 7,5 + 8,0 = 23 * 2,1 = 48,3

# Beispiel 2:
# Schwierigkeitsgrad: 1,6
# Punkte: 7,5 | 7,5 | 7,5 | 7,5 | 7,5 | 7,5 | 7,5
# Gestrichen: 7,5 | 7,5 | 7,5 | 7,5 | 7,5 | 7,5 | 7,5
# result: 7,5 + 7,5 + 7,5 = 22,5 * 1,6 = 36

import random
 
a=float(input('Schwierigkeitsgrad auswählen: '))
 
result=[]
 
for i in range(1,8):
     
    result.append((round(random.uniform(0,10)*2)/2))
  
result=sorted(result)
 
del result[0:2]   
del result[-1:-3:-1]      
print(result)
print('%2.2f' % (sum(result)*a))