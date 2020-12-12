import conexion
import notas.nota as note

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Acciones():
    def Crear(self, usuario):
        print(f"\nOK {usuario[1]}, vamos a crear una nueva nota: ")
        titulo = input("Introduce un titulo: ")
        descripcion = input("Introduce tu nota: ")

        nota = note.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Has creado la nota {nota.titulo}")
        else:
            print(f"Lo siento {usuario.nombre}, ha ocurrido un error y no se ha guardado la nota")
    
    def Mostrar(self, usuario):
        print(f"Estas son tus notas {usuario[1]}:\n")
        nota = note.Nota(usuario[0])
        notas = nota.listar()

        for elem in notas:
            print("***********************************")
            print(elem[2].upper())
            print(elem[3])
            print("***********************************\n")
    
    def Borrar(self, usuario):
        print(f"Qué nota quieres borrar {usuario[1]}?")
        titulo = input("Introduce el titulo de la nota que quieres borrar: ")
        notaBorrar = note.Nota(usuario[0],titulo)

        eliminar = notaBorrar.eliminar()
        if eliminar[0] >= 1:
            print(f"Nota borrada!")
        else:
            print("No tienes ninguna nota con ese titulo")


