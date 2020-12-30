"""
CREAR UN PROGRAMA QUE TENGA:
    - ventana de tamaño fijo no redimensionable
    - un menu
    - diferentes pantallas
    - formulario de añadir productos
    - guardar datos temporalmente
    - mostrar datos listados en la home
    - opcion de salir
"""


from tkinter import *
from tkinter import ttk

def home():
    home_label.config(
        fg="red",
        bg="black",
        font=("MrRobot", 30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0,column=0, columnspan=3)
    for producto in productos:
        if len(producto) == 3:
            producto.append("añadido")
            tabla.insert('', 0, text=producto[0], values=producto[1])
            
    tabla.grid(row=1, column=0, columnspan=3)

    #ocultar las otras pantallas
    add_label.grid_remove()
    formulario.grid_remove()
    info_label.grid_remove()
    datos.grid_remove()

def add():
    add_label.config(
        fg="red",
        bg="black",
        font=("MrRobot", 30),
        padx=40,
        pady=20
    )
    add_label.grid(row=0,column=0, columnspan=2)

    formulario.grid(row=1,column=0)

    #ocultar las otras pantallas
    home_label.grid_remove()
    tabla.grid_remove()
    info_label.grid_remove()
    datos.grid_remove()

def guardarDatos():
    productos.append([
        name_data.get(),
        price_data.get(),
        add_desc_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set(0)
    add_desc_entry.delete("1.0",END)

    home()

def info():
    info_label.config(
        fg="red",
        bg="black",
        font=("MrRobot", 30),
        padx=120,
        pady=20
    )
    info_label.grid(row=0,column=0)
    datos.grid(row=1,column=0)

    #ocultar las otras pantallas    
    add_label.grid_remove()
    home_label.grid_remove()
    formulario.grid_remove()
    tabla.grid_remove()



#definiendo la ventana
ventana = Tk()
ventana.minsize(500,400)
ventana.title("Inventario de productos")
ventana.resizable(0,0)

#crear las pantallas
home_label = Label(ventana, text="Inicio")
add_label = Label(ventana, text="Agregar articulo")
info_label = Label(ventana, text="Acerca de...")
datos = Label(ventana, text="Creado por Ismael Martín Gómez - 30/12/2020")

#menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Acerca de...", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)
#cargar el menu
ventana.config(menu=menu_superior)


#¢ampos del formulario
formulario = Frame(ventana)
name_data = StringVar()
price_data = IntVar()
productos = []


add_name_label = Label(formulario, text="Nombre del articulo")
add_name_entry = Entry(formulario, textvariable=name_data)
add_price_label = Label(formulario, text="Precio del articulo")
add_price_entry = Entry(formulario, textvariable=price_data)
add_desc_label = Label(formulario, text="Descripción del articulo")
add_desc_entry = Text(formulario)
add_desc_entry.config(
    width=30,
    height=5,
    padx=15,
    pady=15
)

boton = Button(formulario, text="Guardar", command=guardarDatos)
boton.config(
    padx=15,
    pady=5,
    bg="green",
    fg="white"
)

add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
add_desc_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
add_desc_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
boton.grid(row=4, column=1, sticky=W)


#listado de productos
tabla = ttk.Treeview(height=12, columns=3)
tabla.heading("#0", text="Nombre", anchor=W)
tabla.heading("#1", text="Precio", anchor=W)


#cargar la pantalla principal
home()
#cargar la ventana
ventana.mainloop()