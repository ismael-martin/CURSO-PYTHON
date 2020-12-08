"""
PROGRAMA QUE AÑADA  VALORES A UNA LISTA SIEMPRE Y CUANDO SU LONGITUD SEA MENOR A 120 (lo hago con 20 porque si no se hace muy largo)
Y MOSTRAR LA LISTA

USAR WHILE Y FOR
"""

lista = []
## USANDO WHILE
while len(lista) <= 19:
    numero = int(input("Dame un numero: "))
    if isinstance(numero, int):
        lista.append(numero)
print(lista)
print(len(lista))

## USANDO FOR
lista2 = []
for elem in range(0,20):
    num = int(input("Dame un numero: "))
    if isinstance(num, int):
        lista2.append(num)
print(lista2)
print(len(lista2))