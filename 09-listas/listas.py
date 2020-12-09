"""
las listas en python son colecciones o conjuntos de datos 
bajo un unico nombre
para acceder a los valores podemos usar un indice numerico
basicamente las listas son arrays en otros lenguajes de programacion

"""

pelicula = "Batman"
#definir listas
peliculas = ["Batman","Spiderman","El señor de los anillos","The room"]
cantantes = list(('2pac','drake','Kase.o')) #aqui estoy pasando una tupla para despues convertirla en lista
"""
las tuplas son listas pero con elementos NO MODIFICABLES
"""
years = list(range(2020,2039))
variada = ['Isma', 99, 4.5, True]

"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

#indices de las listas
print(peliculas[1]) #accedo al indice 1 de la lista peliculas
print(peliculas[-2]) #accedo al indice de la lista que indico desde el final
print(peliculas[1:3]) #accedo a un rango de indices de la lista

#puedo reasignar valores a los elementos de la lista accediendo desde su indice
print(peliculas)
peliculas[3] = "Gran Torino"
print(peliculas)

#añadir contenido a una lista
peliculas.append("Star Wars")
print(peliculas)

#recorrer y mostrar una lista con bucles
#esto es como un foreach en php
for peli in peliculas:
    print(f"{peliculas.index(peli)} {peli}")

nueva_peli = ""
while nueva_peli != "parar":
    nueva_peli = input("Introduce la nueva pelicula: ")
    
    if nueva_peli != "parar":
        peliculas.append(nueva_peli)

for peli in peliculas:
    print(f"{peliculas.index(peli)} {peli}")



#lista multidimensional
print("\n@@@@@@@@@ LISTADO DE CONTACTOS @@@@@@@@@\n")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Paco',
        'paco@paquito.es'
    ],
    [
        'Felipe',
        'erfeli_69@sexo.com'
    ]
]

for contacto in contactos:
    for dato in contacto:
        print(dato)
    print("\n")