# Input 

C1 = int(input("Ingrese el valor del primer capital: "))
C2 = int(input("Ingrese el valor del segundo capital: "))
C3 = int(input("Ingrese el valor del capital a llegar: "))
M = 0
capital_final = C1 + C2 

# Prossesing 

while capital_final < C3: 
    C1 = C1 + (C1 * 0.03)
    C2 = C2 + (C2 * 0.04)
    capital_final = C1 + C2
    M = M + 1 

# Output 

print("El numero de meses necesario para alcanzar el capital final es: ", M)
