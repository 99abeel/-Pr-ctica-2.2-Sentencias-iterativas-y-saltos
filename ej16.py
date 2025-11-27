# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar 
# cuál fue el mayor número ingresado. 

def acumuladorNumeros(numero):
    mayor = 0
    while numero != 0:
        if numero > mayor:
            mayor = numero
        numero = int(input("Introduce numeros enteros (0 para salir): "))

    return mayor

def main():
    numero = int(input("Introduce numeros enteros (0 para salir): "))
    total = acumuladorNumeros(numero)
    print(f"El numero mayor que has introducido ha sido {total}")


if __name__ == "__main__":
    main()