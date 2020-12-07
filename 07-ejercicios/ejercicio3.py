"""
IMPRIMIR POR PANTALLA LOS CUADRADOS DE LOS 60 PRIMEROS NUMEROS NATURALES

CON FOR Y CON WHILE
"""

#FOR
num = 0
for num in range(1,61):
    print(num * num)
    num += 1

#WHILE
num = 0
while num <= 60:
    print(num * num)
    num += 1
