# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
# el número de años, y muestre por pantalla el capital obtenido en la inversión cada año 
# que dura la inversión. 
# Formula para calcular El capital tras un año. 
# amount *= 1 + interest / 100 
# En donde: 
# - amount: Cantidad a invertir 
# - interest: Interes porcentual anual 

def CalculoCapital(amount, interest, año):
    if amount < 0:
        raise NameError("No puedes introducir dinero que no existe!")
    if interest < 0:
        raise NameError("No puedes introducir un interes negativo!")
    if año < 0:
        raise NameError("No puedes introducir años negativos!")
    for i in range (1, año+1):
        amount *= 1 + interest / 100
        print(f"Año {i}: {amount}€")
    
    return amount

def main():
    try:
        cantidad = float(input("Introduce la cantidad que quieres invertir: "))
        interes = int(input("Introduce el % que quieres: "))
        año = int(input("Introduce los años que quieres ese interes: "))

        resultado = CalculoCapital(cantidad, interes, año)
        print(f"Has obtenido un total de {resultado}€")

    except ValueError:
        print("Has introducido un caracter incorrecto, introduce lo que se te pide.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()