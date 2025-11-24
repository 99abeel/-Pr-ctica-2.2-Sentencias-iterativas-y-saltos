# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
# muestre por pantalla el número de veces que aparece la letra en la frase. 

def contadorPalabra(frase, letra):
    contador = 0
    for c in frase:
        if c == letra:
            contador +=1
    
    return contador
        
            

def main():
    frase = input("Escribe una frase: ")
    letra = input("Escribe una letra: ")

    contador = contadorPalabra(frase, letra)

    print(f"En la frase/palabra: {frase}, hay {contador} letras {letra}.")

if __name__ == "__main__":
    main()