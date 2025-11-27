# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3
# finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 
# 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a 
# mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las 
# opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión 
# del menú y el programa finalizará. 


opcion = ""   

while opcion != "3":
    print("\n=== MENÚ PRINCIPAL ===")
    print("1 - Comenzar programa")
    print("2 - Imprimir texto")
    print("3 - Finalizar programa")

    opcion = input("Selecciona una opcion (1, 2 o 3): ")

    match opcion:
        case "1":
            print("Has elegido la opcion 1: Comenzando el programa...")

        case "2":
            print("Has elegido la opcion 2: Imprimiendo texto...")

        case "3":
            print("Has elegido la opcion 3: Finalizando el programa...")

        case _:
            print("Opcion incorrecta. Intentalo de nuevo.")