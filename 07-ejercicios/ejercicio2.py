"""
MOSTRAR POR PANTALLA TODOS LOS NUMERO PARES DEL 1 AL 120
"""
#con while
contador = 1
while contador <= 120:
    if contador % 2 == 0:
        print(contador)
    contador += 1

#con for
contador = 1
for contador in range(1,121):
    if contador % 2 == 0:
        print(contador)
    contador += 1