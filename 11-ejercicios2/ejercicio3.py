"""
COMPROBAR SI UNA VARIABLE ESTÁ VACIA, SI LO ESTÁ, RELLENAR CON TEXTO EN MINUSCULAS E IMPRIMIRLO POR PANTALLA EN MAYUSCULAS
"""

def compVariable(var):
    if len(var.strip()) == 0: #limpio espacios y compruebo si tiene contenido
        var = "Esta variable estaba VACIA"
        var = var.lower()
        return var
    else:
        print("La variable tiene contenido, no hace falta hacer nada")
        return var

vacia = ""
contenido = "Variable"

print(compVariable(vacia).upper())

print(compVariable(contenido).upper())