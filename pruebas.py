def mostrarNumero(a):
    for i in range(1, a + 1):
        if i % 2 != 0:
            print(i, end=", ")
    return a

def main():
    numero = int(input("Introduce un numero entero:"))
    mostrarNumero(numero)

main()