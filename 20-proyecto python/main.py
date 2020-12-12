"""
PROYECTO PYTHON + MYSQL
-Abrir asistente
-Login o Registro
-Registro crea usuario en la BBDD
-Login identifica al usuario y nos pregunta:
-Crear nota, mostrar notas, borrar notas
"""
from usuarios import acciones
#un print con triple comilla me permite sacar por pantalla texto con saltos de linea
def inicio():

    print("""
    BIENVENIDO!
    ¿Qué deseas hacer?:
        - Registrarte? (registro o 1)
        - Acceder? (login o 2)
    """)

    accion = input(">")
    hazEl = acciones.Acciones()

    if accion == "registro" or accion == "1":
        hazEl.registro()
        hazEl.login()


    elif accion == "login" or accion == "2":
        hazEl.login()

    else: 
        print("comando desconocido")
        inicio()

inicio()