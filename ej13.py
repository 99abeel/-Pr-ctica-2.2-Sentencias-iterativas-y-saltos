# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que 
# el usuario escriba “salir” que terminará.

def acumulacionPalabras(palabra):
    acumulador = ""
    while palabra != "salir":
        acumulador += palabra + " "
        print(acumulador)
        palabra = input("Escribe una palabra (salir para terminar): ")

    return acumulador
    

def main():
    palabra = input("Escribe una palabra (salir para terminar): ")
    acumulacionPalabras(palabra)

if __name__ == "__main__":
    main()