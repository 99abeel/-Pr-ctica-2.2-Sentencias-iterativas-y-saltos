# Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo, de altura el número introducido.  
# * 
# ** 
# *** 
# **** 
# *****

def dibujarTringulo(a):
    for i in range(1, a+1):
        print("*" * i)

def main():
    numero = int(input("introduce un numero: "))

    dibujarTringulo(numero)

if __name__ == "__main__":
    main()