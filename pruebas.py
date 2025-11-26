def acumulacionPalabras(palabra):
    acumulador = ""
    while palabra != "salir":
        acumulador += palabra
        print(acumulador)
        palabra = input("Escribe una palabra (salir para terminar): ")  # ← actualizar palabra
    
    return acumulador


def main():
    palabra = input("Escribe una palabra (salir para terminar): ")
    acumulacionPalabras(palabra)

if __name__ == "__main__":
    main()
