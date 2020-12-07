"""
MOSTRAR POR PANTALLA TODOS LOS NUMEROS IMPARES ENTRE LOS DOS NUMERO QUE 
ELIJA EL USUARIO
"""

num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

if num1 < num2:
    for cont in range(num1,num2+1):
        if cont % 2 != 0:
            print(cont)
else:
    for cont in range(num2,num1+1):
        if cont % 2 != 0:
            print(cont)