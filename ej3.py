# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla todos los números impares desde 1 hasta ese número separados por comas.

def mostrarNumero(a):
    if a < 0:
             raise NameError("No puedes introducir numeros negativos")
    
    for i in range (1, a+1):
        if i % 2 != 0:
            print(i, end=", ")       
    return a

def main():
    try:
        numero = int(input("Introduce un numero entero: "))
        mostrarNumero(numero)
    except ValueError:
        print("El numero introducido no es valido.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
