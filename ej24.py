from sympy import isprime

numero=1
primos = 0

while (numero!=0):
    numero=int(input("Introduce un numero(0 para terminar): "))
    if numero == 1:
        print("Error, el 1 no vale")
    else:
        numero=abs(numero)
        if isprime(numero):
            primos+=1

print(f"Has introducido {primos} numeros primos.")