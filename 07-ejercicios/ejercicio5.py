"""
MOSTRAR TODOS LOS NUMEROS ENTRE LOS DOS QUE NOS PASE EL USUARIO Y MOSTRAR
POR PANTALLA
"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 < num2:
    for rango in range(num1,num2+1):
        print(rango)
        rango += 1
else:
    for rango in range(num2,num1+1):
        print(rango)
        rango += 1