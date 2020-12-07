#tipos de datos
#defino una función para mostrar el valor de la variable y su tipo
def imprimirVarType (variable):
    print(variable)
    print(type(variable))


nada = None #variable vacía
imprimirVarType(nada) #imprimir variable
#imprimir tipo de dato (NoneType)

cadena = "hola soy isma"
imprimirVarType(cadena)
#(str)

entero = 99
imprimirVarType(entero)
#(int)

flotante = 85.6
imprimirVarType(flotante)
#(float)

booleano = True #o False
imprimirVarType(booleano)
#(bool)

lista = [10,20,30,200] #array
imprimirVarType(lista)
#(list)

listaString = [44,"hamilton",77,"bottas",14,"alonso"]
imprimirVarType(listaString) #(list)

tuplaNoCambia = {"Master", "en", "Python"}
imprimirVarType(tuplaNoCambia) #(set)

diccionario = {
    "nombre": "Ismael",
    "apellidos": "Martín"
}
imprimirVarType(diccionario) #(dict)

rango = range(9)
imprimirVarType(rango) #range

dato_byte = b"Probando"
imprimirVarType(dato_byte) #(bytes)

#cambiar de un tipo a otro
texto = "hola soy un texto"
numerito = 6
#para concatenar strings con enteros usamos str(variableNoString)
print(texto + " " + str(numerito))

#para pasar a diferentes tipos de datos podemos usar:
"""
int() para pasar a entero
str() para pasar a string
float() para pasar a flotante

"""