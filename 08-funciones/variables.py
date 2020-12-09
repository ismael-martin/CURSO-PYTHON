"""
diferencias entre variables globales y locales
variable global: son las que son accesibles desde cualquier parte del código
variables locales: son sólamente utilizables dentro de una función 
"""

#VARIABLES GLOBALES
texto = "Doy el callo por dinero, yo trabajo por dinero, no se que y no se cuantos pero a mi dame el dinero"

print(texto)

def holaMundo():
    print(texto)
    print("La variable texto es global")
    year = 2020
    print(year)
    print("year es una variable local, fuera de la función no es accesible a no ser que la devuelva con return")
    global website
    website = "www.getbrit.es"

holaMundo()

print(website) #puedo ejecutar este print porque he declarado website como global dentro de la función