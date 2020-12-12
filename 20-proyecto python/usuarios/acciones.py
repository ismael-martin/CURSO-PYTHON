import usuarios.usuarios as user
import notas.acciones

class Acciones():
    def registro(self):
        print("\nOK! Vamos a registrarte en el sistema...")
        nombre = input("Nombre*: ")
        apellidos = input("Apellidos*: ")
        email = input("Email*: ")
        contrasena = input("Contraseña*: ")
        usuario = user.Usuario(nombre,apellidos,email,contrasena)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Usuario {registro[1].nombre} registrado correctamente")
        else:
            print("No se ha podido registrar al usuario")
    
    def login(self):
        print("\nIdentificate: ")
        try:
            email = input("Email*: ")
            contrasena = input("Contraseña*: ")

            usuario = user.Usuario('','',email,contrasena)
            registro = usuario.identificar()

            if email == registro[3]:
                print(f"Bienvenido {registro[1]}")
                self.proximasAcciones(registro)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login in correcto, intentalo de nuevo")

    def proximasAcciones(self, user):
        print("""
        \nACCIONES DISPONIBLES:
            - Crear nota (crear o 1)
            - Mostrar tus notas (mostrar o 2)
            - Eliminar nota (eliminar o 3)
            - Salir (salir o 4)
        """)

        accion = input(">")
        hazEl = notas.acciones.Acciones()

        if accion == "crear" or accion == "1":
            hazEl.Crear(user)
            self.proximasAcciones(user)
        elif accion == "mostrar" or accion == "2":
            hazEl.Mostrar(user)
            self.proximasAcciones(user)
        elif accion == "eliminar" or accion == "3":
            hazEl.Borrar(user)
            self.proximasAcciones(user)
        elif accion == "salir" or accion == "4":
            print("Hasta pronto!")
            exit()
        else: 
            print("comando desconocido") 
            self.proximasAcciones(user)