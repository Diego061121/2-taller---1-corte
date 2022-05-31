# Input 

N = int(input("Digite el valor de N: "))
F = 1

# Prossesing 

if N > 0: 
    while N > 1: 
        F = F * N 
        N = N - 1 

# Output 

print("El factorial de ", N, " Es igual a ", F)