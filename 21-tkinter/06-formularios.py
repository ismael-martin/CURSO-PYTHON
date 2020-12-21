from tkinter import *

ventana = Tk()
ventana.title("Formularios en tkinter")
ventana.geometry("700x400")

##encabezado
encabezado = Label(ventana, text="Formularios con tkinter | Ismael Martín")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0,column=0, columnspan=15, sticky=E)

#label para el campo (NOMBRE)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

#campo de texto (NOMBRE)
campoTexto = Entry(ventana)
campoTexto.config(
    width=20,
    justify=RIGHT,
    state=NORMAL
)
campoTexto.grid(row=1, column=1 ,padx=5, pady=5)


#label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#campo de texto (apellidos)
campoTexto = Entry(ventana)
campoTexto.config(
    width=20,
    justify=LEFT,
    state=DISABLED
)
campoTexto.grid(row=2, column=1 ,padx=5, pady=5)


label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

#campo de texto grande (descripción)
campo_grande = Text(ventana)
campo_grande.grid(row=3,column=1)
campo_grande.config(
    width=20,
    height=5,
    font=("Arial",12),
    padx=15,
    pady=15
)

#boton
Label(ventana).grid(row=4,column=1)
boton = Button(ventana, text="Enviar")
boton.grid(row=5,column=1, sticky=W)
boton.config(
    padx=10,
    pady=10,
    bg="green",
    fg="white"
)
ventana.mainloop()