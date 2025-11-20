# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 

contraseña = "hola123"

def preguntarContraseña(pedir):

    while contraseña != pedir.lower():
        print("Contraseña incorrecta, intentalo de nuevo.")
        pedir = input("Introduce la contraseña: ")
    print("Has acertado la contraseña.")

def main():
    
    contra = input("Escribe la contraseña: ")
    preguntarContraseña(contra)

if __name__ == "__main__":
    main()