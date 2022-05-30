"""Programa para calcular el factorial de un numero N"""


# Input 

def factorial(N):
    if N >= 1:
 
        f = N 
        while N>=2:
            N = N - 1
            f = f * (N)

        print("el factorial es: ",f)

    if N == 0:
        print("el factorial es 1")
 
 
factorial(int(input("ingrese el numero para calcular su factorial: ")))