import mysql.connector

#conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    passwd = "admin",
    database = "python"
)

##La conexion es correcta??
#print(database) para comprobarlo

#crear cursor para ejecutar consultas
cursor = database.cursor(buffered=True)

#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS python")

#listar bbdd
#cursor.execute("SHOW DATABASES")



cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for tb in cursor:
    print(tb)

#insertar datos
"""cursor.execute("""
#insert into vehiculos values(null,'Lamborghini','Aventador',1500000)
""")"""
#database.commit()


#insertar multiples datos
coches = [
    ('Seat','Ibiza', 20000),
    ('Fiat','500', 15000),
    ('Mercedes','SLS', 250000),
    ('Renault','Clio', 10000),
    ('McLaren','MCL35', 20000000),
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)
#database.commit()

#COMENTO LAS LINEAS DE INSERT PARA QUE NO ME INTRODUZCA DATOS CADA VEZ QUE EJECUTO EL CODIGO

#consulta
#cursor.execute("SELECT * from vehiculos")
#cursor.execute("SELECT * from vehiculos where precio <= 15000")
cursor.execute("SELECT * from vehiculos where precio <= 15000 and marca = 'Fiat'")

result = cursor.fetchall()
for coche in result:
    print(f"MARCA: {coche[1]}, PRECIO: {coche[3]}")

cursor.execute("SELECT * from vehiculos")
unCoche = cursor.fetchone()
print(unCoche)

#borrar registros
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()
print(cursor.rowcount, "BORRADOS!")#contar registros borrados

cursor.execute("update vehiculos set modelo = 'Senna' where marca = 'McLaren'")
database.commit()