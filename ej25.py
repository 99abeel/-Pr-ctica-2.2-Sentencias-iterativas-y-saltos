# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
# Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea 
# uno o más.

frase = input("Introduce una frase: ")

palabras = frase.split(" ")

cantidad_palabras = 0
palabra_mas_larga = ""
longitud_maxima = 0

for palabra in palabras:
    cantidad_palabras += 1
    if len(palabra) > longitud_maxima:
        longitud_maxima = len(palabra)
        palabra_mas_larga = palabra

print("Cantidad de palabras:", cantidad_palabras)
print("Palabra mas larga: ", palabra_mas_larga)