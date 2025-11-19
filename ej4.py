# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla la cuenta atrás desde ese número hasta cero separados por comas. 

def contarAtras(a):
    if a < 0:
        raise NameError("No puedes introducir numeros negativos.")
    for i in range (a, 0, -1):
        print(i, end=", ")
    
    return i

def main():
    try:
        numero = int(input("Introduce un numero: ")) 
        contarAtras(numero)

    except ValueError:
        print("Introduce un numero entero!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
