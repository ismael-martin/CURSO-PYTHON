"""
CREAR CUATRO VARIABLES DE TIPOS DIFERENTES Y MOSTRAR POR PANTALLA DE QUE TIPO SON
"""

def tipoVariable(var,tipo):
    test = isinstance(var,tipo)
    result = ""
    if test:
        result = f"Este dato es del tipo {type(var)}"
    else:
        result = "La variable no es del tipo correcto"
    return result

entero = 1
lista = [1,2,3,4,"prueba",True,7,"",None]
cadena = "Esto es una cadena"
binario = True
print(tipoVariable(entero, int))
print(tipoVariable(lista, list))
print(tipoVariable(cadena, str))
print(tipoVariable(binario, str))