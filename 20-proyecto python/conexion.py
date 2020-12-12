import mysql.connector
#conexion
def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        passwd = "admin",
        database = "proyecto_python",
        port = 3306
    )
    cursor = database.cursor(buffered=True)

    return [database, cursor]