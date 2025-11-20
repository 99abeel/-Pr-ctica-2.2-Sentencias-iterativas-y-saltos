# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a 
# una las letras de la palabra introducida empezando por la última.

def palabraInvertida(a):
    for i in a [::-1]:
        print(i)

def main():
    palabra = input("Introduce una palabra: ")

    palabraInvertida(palabra)

if __name__ == "__main__":
    main()