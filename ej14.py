# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar 
# la sumatoria de todos los números ingresados.

def acumuladorNumeros(numero):
    acumulador = 0
    while numero != 0:
        acumulador += numero
        numero = int(input("Introduce numeros enteros (0 para salir): "))

    return acumulador

def main():
    numero = int(input("Introduce numeros enteros (0 para salir): "))
    total = acumuladorNumeros(numero)
    print(f"El total de numeros que has introducido ha sido {total}")


if __name__ == "__main__":
    main()