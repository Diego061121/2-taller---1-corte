# input

numero = int(input("Digite el numero: "))

# procesing 

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10 * numero + n % 10
        n = n // 10
    return numero
    
numero_invertido = invertir_numero(numero)

# output 

if numero == numero_invertido:
    print("El numero", numero, " es capicúa")