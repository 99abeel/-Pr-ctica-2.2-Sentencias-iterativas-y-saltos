linea_actual = ""
lineas_completas = 0
entrada = ""

while entrada != '*':
    entrada = input("Titulo: ")
    if entrada == '/':
        total_digitos = 0
        for titulo in linea_actual:
            for caracter in titulo:
                if caracter in "0123456789":
                    total_digitos += 1
        print("Digitos numericos en esta linea:", total_digitos)
        lineas_completas += 1
        linea_actual = ""
    else:
        linea_actual = linea_actual + entrada

print("\nTotal de lineas completas ingresadas:", lineas_completas)