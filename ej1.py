# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def mostrarBuclePalabra(a):
    for i in range (0, 10):
        print(a)
    return a

def main():
    palabra = input("Introduce una palabra: ")

    mostrarBuclePalabra(palabra)


if __name__ == "__main__":
    main()
