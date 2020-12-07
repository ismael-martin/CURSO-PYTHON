"""
MOSTRAR TODAS LAS TABLAS DE MULTIPLICAR DEL 1 AL 10
"""

def tablaMultiplicar(numero):
    contador = 1
    print(f"\n\n###### TABLA DEL {numero} ######")
    while contador <= 10:
        print(f"{contador} x {numero} = {contador * numero}")
        contador += 1

for num in range(1,11):
    tablaMultiplicar(num)