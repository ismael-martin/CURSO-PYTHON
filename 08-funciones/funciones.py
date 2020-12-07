"""
a lo largo del curso ya he usado funciones porque ya sabía hacerlas
son instrucciones agrupadas que pueden reutilizarse invocando la funcion tantas
veces como sea necesario

la nomenclatura es:

def nombreDeLaFuncion(parametros,separados,comas):
    instrucciones

nombreDeLaFuncion(variable1,variable2,variable3)
nombreDeLaFuncion(var1,var2,var3)
"""

#ejemplo 1

print("EJEMPLO 1")

#defino la función
def muestraNombre(nombre):
    print(nombre)

#invoco la función
muestraNombre("Victor")
muestraNombre("Ismael")
muestraNombre("pepe")

#ejemplo 2
print("\nEJEMPLO 2")

def tablaMultiplicar(numero):
    print(f"\nTABLA DEL {numero}")
    for cont in range(11):
        op = numero*cont
        print(f"{numero} x {cont} = {op}")

tabla = int(input("De qué numero quieres la tabla?: "))
tablaMultiplicar(tabla)