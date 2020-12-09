"""
INTRODUCIR LA NOTA DE 15 ALUMNOS Y SACAR POR PANTALLA CUANTOS HAN APROBADO 
Y CUANTOS HAN SUSPENDIDO
"""

aprobados = 0
suspensos = 0
cont = 1

while cont <= 15:
    nota = int(input(f"Introduce la nota del alumno {cont}: "))
    if nota >= 0 and nota < 5:
        suspensos += 1
        cont += 1
    elif nota >= 5 and nota <=10:
        aprobados += 1
        cont += 1
    else:
        print("Has introducido una nota erronea")

print(f"Han aprobado {aprobados} alumnos y los otros {suspensos} han suspendido")