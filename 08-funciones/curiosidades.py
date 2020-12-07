#es recomendable declarar las funciones al principio del código

def miPrimeraFuncion():
    saludo = "Hola que tal?"
    return saludo
    #es recomendable que las funciones siempre tengan return

def miSegundaFuncion(nombre, apellidos):
    saludo = f"Bienvenido {nombre} {apellidos}"
    return saludo
    #si uso variables globales dentro de mis funciones siempre debo invocarlas 
    #despues de declarar las variables, si no el código falla
    #lo mejor que puedo hacer es hacer funciones que reciban los parametros directamente 
    #en lugar de acceder a las variables globales

nombre = "Ismael"
apellidos = "Martín Gómez"

print("Hola mundo")
print(f"Bienvenido {nombre} {apellidos}")

