# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
# un número primo o no. 

def primo(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True
    
def main():
    n = int(input("Introduce un numero: "))

    if primo(n):
        print("El numero es primo.")
    else: 
        print("El numero no es primo.")

if __name__ == "__main__":
    main()
