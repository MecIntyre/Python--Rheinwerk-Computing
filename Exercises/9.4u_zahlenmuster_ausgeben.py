# Schreibe ein Programm, das folgendes ausgibt:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

for zeile in range (5, 0, -1):
    for spalte in range (1, zeile +1):
            print(f"{spalte:2d}", end="")

    print("")
            
        
