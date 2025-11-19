# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
# años que ha cumplido (desde 1 hasta su edad). 

def mostrarEdad(a):
    contador = 0
    for i in range (1, a+1):
        contador += 1
        print(f"has cumplido {i} años")
    return i

def main():
    edad = int(input("Introduce tu edad: "))

    mostrarEdad(edad)

if __name__ == "__main__":
    main()
