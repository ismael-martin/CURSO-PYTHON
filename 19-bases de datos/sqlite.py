"""
ELEMENTOS QUE HAY EN LA BASE DE DATOS
Consta de TABLAS, que esta formada por columnas, filas y campos

para conectar a bases de datos con sqlite:

"""

import sqlite3

#conexion
conexion = sqlite3.connect('./19-bases de datos/pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT not null,
                    titulo VARCHAR(225),   
                    descripcion text,
                    precio int(5))""")

#guardar cambios
conexion.commit()

"""
#insertar datos y guardar
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
#print(productos)
for producto in productos:
    print("ID: ",producto[0])
    print("Titulo: ",producto[1])
    print("Descripción: ",producto[2])
    print("\n")

cursor.execute("SELECT * FROM productos")
prod = cursor.fetchone()
print(prod)

print("###### BORRO ELEMENTOS Y CREO OTROS NUEVOS ######\n\n")

#borrar registros
cursor.execute("delete from productos") #BORRA TODOS LOS REGISTROS
conexion.commit()

#Insertar varios registros de golpe
registros = [
    ("Ordenador portátil", "Buen PC", 700),
    ("Telefono móvil", "Buen Movil", 850),
    ("Tostadora mierder", "Buena Tostadora", 20),
    ("Pedrolo inutil", "Buena Piedra", 0),
]
cursor.executemany("insert into productos values (null,?,?,?)",registros)
conexion.commit()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
#print(productos)
for producto in productos:
    print("ID: ",producto[0])
    print("Titulo: ",producto[1])
    print("Descripción: ",producto[2])
    print("\n")

#cerrar conexion
conexion.close()