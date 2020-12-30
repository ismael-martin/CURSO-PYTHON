"""
A CONTINUACIÓN EL CODIGO DE CONFIGURACIÓN DE MAS ELEMENTOS DE FORMULARIO
    - CHECKBOX
    - RADIO BUTTON
    - OPTION MENU

"""

from tkinter import *

ventana = Tk()


encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,pady=15,fg="white",bg="green",font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=N)

web = IntVar()
movil = IntVar()

#BOTONES CHECK
def mostrarProfesion():
    text = ""
    if web.get():
        text+="Desarrollo Web"
    
    if movil.get():
        if web.get():
            text+=" y Desarrollo Movil"
        else:
            text+="Desarrollo Movil"
    
    mostrar.config(
        text=text,bg="green",fg="white"
    )

Label(ventana, text="¿A qué te dedicas?").grid(row=1,column=0)
Checkbutton(
    ventana, 
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion).grid(row=2,column=0)

Checkbutton(
    ventana, 
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion).grid(row=3,column=0)

mostrar = Label(ventana)
mostrar.grid(row=4,column=0)

#RADIO BUTTONS
def marcar():
    marcado.config(
        text=opcion.get()
    )
opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cual es tu genero?").grid(row=5)
Radiobutton(
    ventana, 
    text="Masculuno",
    variable=opcion,
    value="Masculino",
    command=marcar).grid(row=6)
Radiobutton(
    ventana, 
    text="Femenino",
    variable=opcion,
    value="Femenino",
    command=marcar).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)



#OPTION MENU
def seleccion():
    seleccionado.config(
        text=opcion.get()
    )


Label(ventana, text="¿Cual es tu genero?").grid(row=9)
opcion = StringVar()
opcion.set("Selecciona una")
select = OptionMenu(ventana,opcion, "opcion 1", "opcion 2", "opcion 3")
select.grid(row=10)

Button(ventana, text="Ver selección", command=seleccion).grid(row=11)

seleccionado = Label(ventana)
seleccionado.grid(row=12)



ventana.mainloop()