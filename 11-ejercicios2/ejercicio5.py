"""
CREAR UNA LISTA CON EL CONTENIDO DE ESTA TABLA
ACCION      AVENTURA            DEPORTES
GTA         ASSASSINS CREED     FIFA21
COD         CRASH BANDICOOT     FORMULA 1 21
PUBG        THE LAST OF US      MOTO GP 21

MOSTRAR LA INFORMACIÓN ORDENADA POR CATEGORIAS DE JUEGOS

"""
#DEFINO UNA FUNCIÓN PARA MOSTRAR LA INFORMACIÓN ORDENADA POR CATEGORÍAS
def juegosCategoria(lista,categoria):
    inventario = "Los juegos de la categoría " + categoria + " son: \n"
    for elem in lista:
        if elem["categoria"] == categoria:
            inventario += elem["nombre"] + "\n"
    inventario += "\n"
    return inventario

#CREO LA LISTA
juegos = [
    {
        "nombre":"GTA V",
        "categoria":"ACCIÓN"

    },
    {
        "nombre":"ASSASSINS CREED",
        "categoria":"AVENTURA"

    },
    {
        "nombre":"FIFA21",
        "categoria":"DEPORTES"

    },
    {
        "nombre":"COD",
        "categoria":"ACCIÓN"

    },
    {
        "nombre":"CRASH BANDICOOT",
        "categoria":"AVENTURA"

    },
    {
        "nombre":"FORMULA 1 21",
        "categoria":"DEPORTES"

    },
    {
        "nombre":"PUBG",
        "categoria":"ACCIÓN"

    },
    {
        "nombre":"THE LAST OF US",
        "categoria":"AVENTURA"

    },
    {
        "nombre":"MOTO GP 21",
        "categoria":"DEPORTES"

    }
]

#MUESTRO LOS JUEGOS DEL DICCIONARIO SEGÚN SU CATEGORÍA
print(juegosCategoria(juegos,"ACCIÓN"))

print(juegosCategoria(juegos,"DEPORTES"))

print(juegosCategoria(juegos,"AVENTURA"))