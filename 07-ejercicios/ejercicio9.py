"""
PEDIR UN NUMERO INDEFINIDAMENTE HASTA QUE EL USUARIO INTRODUZCA 1111
"""

contador = 0
while contador != 1111:
    numero = int(input("Introduce un numero, si quieres que pare dame el 1111: "))
    print("El numero que me has dado es "+ str(numero))
    contador = numero
else:
    print("Contraseña correcta, ya paro")