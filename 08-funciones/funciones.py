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

#ejemplo 3, parametros opcionales
print("\nEJEMPLO 3")

def getEmpleado(nombre, dni = None):#el parametro opcional es dni
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")

getEmpleado("Ismael","12345")

getEmpleado("Victor")#no paso el segundo parametro pero aun así la funcion funciona xD

#ejemplo 4, return
print("\nEJEMPLO 4")

def saludame(nombre):
    saludo = f"Bienvenido {nombre}"
    return saludo

print(saludame("Isma"))

#ejemplo 5 con todo lo aprendido
print("\nEJEMPLO 5")
def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2

    cadena = ""
    cadena += "Suma: "+ str(suma)
    cadena += "\nResta: "+ str(resta)
    if basicas == True:
        cadena += "\nMultiplicación: "+ str(multi)
        cadena += "\nDivisión: "+ str(divi)
    
    return cadena
print(calculadora(5,5))
print(calculadora(2,3,True))

#ejemplo 6 ORIGEN: Funciones dentro de Funciones
print("\nEJEMPLO 6")

def getNombre(nombre):
    text = f"El nombre es {nombre}"
    return text

def getApellidos(ape):
    text = f"Los apellidos son {ape}"
    return text

def nombreCompleto(name, surname):
    text = getNombre(name) + "\n" + getApellidos(surname)
    return text

print(nombreCompleto("ismael","martín"))

#ejemplo 7, funciones lambda
print("\nEJEMPLO 7")

dime_el_year = lambda year: f"El año es {year}"
#son funciones rapidas que se definen en una linea

print(dime_el_year(2020))
