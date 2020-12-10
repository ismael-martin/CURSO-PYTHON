"""
PROYECTO PYTHON + MYSQL
-Abrir asistente
-Login o Registro
-Registro crea usuario en la BBDD
-Login identifica al usuario y nos pregunta:
-Crear nota, mostrar notas, borrar notas
"""
#un print con triple comilla me permite sacar por pantalla texto con saltos de linea
print("""
BIENVENIDO!
¿Qué deseas hacer?:
    - Registrarte? (registro o 1)
    - Acceder? (login o 2)
""")

accion = input(">")

if accion == "registro" or accion == "1":
    print("\nOK! Vamos a registrarte en el sistema...")
    nombre = input("Nombre*: ")
    apellidos = input("Apellidos*: ")
    email = input("Email*: ")
    contraseña = input("Contraseña*: ")
elif accion == "login" or "2":
    print("\nIdentificate: ")