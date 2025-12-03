# Escribe un programa que pida por teclado un día de la semana y que diga qué asignatura
# toca a primera hora ese día.

dia = (input("Escribe un dia de la semana (lunes-viernes): "))

dia.lower()
if dia == 'lunes':
    print("Toca Base de Datos.")
elif dia == 'martes':
    print("Toca Base de Datos.")
elif dia == 'miercoles':
    print("Toca Programación")
elif dia == 'jueves':
    print("Toca Sostenibilidad")
elif dia == 'viernes':
    print("Toca IPE.")
else:
    print("Introduce el día de la semana que se indica en los parentesis!")