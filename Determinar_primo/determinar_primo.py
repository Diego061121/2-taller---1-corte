# Input 

N = int(input("Ingrese el valor de N: "))
C = 0
X = 1 

# Prossesing 

while X < N: 
    if N % X == 0: 
        C = C + 1
    X = X + 1 

if C == 2: 
    print("El numero no es primo")

else: 
    print("El numero es primo")

