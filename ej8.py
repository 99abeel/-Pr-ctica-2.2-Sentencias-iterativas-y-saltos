# Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo.  
# 1 
# 3 1 
# 5 3 1 
# 7 5 3 1 
# 9 7 5 3 1 

      
def piramide(numero):
    for i in range (1, numero+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print()
            

def main():
    n = int(input("Introduce un numero: "))
    piramide(n)

if __name__ == "__main__":
    main()


