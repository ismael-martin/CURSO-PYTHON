"""
SET es un tipo de dato para tener una colección de valores pero sin indice ni orden
"""

personas = {
    "Isma",
    "Javi",
    "Batracio",
    "Willyrex"
}

print(personas) #cada vez que ejecute print el orden cambia
personas.add("Sr. Meeseks")
print(type(personas))
personas.remove("Willyrex")

print(personas)