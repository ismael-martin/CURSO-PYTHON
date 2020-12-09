"""
PROGRAMA QUE DIGA EL TANTO PORCIENTO DE UN NUMERO QUE NOS DÉ EL USUARIO

Cuanto es el x% de y numero
"""

numero = float(input("Introduce un número: "))
porcentaje = float(input("Qué tanto porciento quieres?: "))

tantoPorciento = porcentaje / 100

print(f"El {porcentaje}% de {numero} es {numero*tantoPorciento}")