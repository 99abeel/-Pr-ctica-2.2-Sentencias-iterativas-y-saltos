# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo 
# componen. 

def sumaDigitos(num):
    suma = 0

    while (num>0):
        suma+=num%10
        num=num//10

    return suma

def main():
    numero=int(input("Introduce número: "))
    print(f"La suma de los digitos de este numero es: {sumaDigitos(numero)}")

if __name__ == "__main__":
    main()