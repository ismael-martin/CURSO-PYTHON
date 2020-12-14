from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.pack(side=BOTTOM)


texto = Label(ventana, text = "TEXTO BASICO")
#la llamada a la función pruebas() de la linea anterior funncionaria tambien si le pasamos los paramatreos desordenados usando keywords
texto.config(#para modificar el aspecto de los textos podemos usar propiedades como las siguientes, aunque hay mas
    fg="red",
    bg="orange",
    padx=10,
    pady=20,
    font=("Console", 20),
    justify=RIGHT,
    width=30,
    height=4,
    cursor="spider"

)
texto.pack(side=LEFT,expand=YES)

texto = Label(ventana, text = "Basico 1")
texto.config(#para modificar el aspecto de los textos podemos usar propiedades como las siguientes, aunque hay mas
    fg="blue",
    bg="grey",
    padx=15,
    pady=10,
    font=("Console", 10),
    justify=LEFT,
    width=30,
    height=4,
    cursor="circle"

)
texto.pack(anchor=CENTER)

texto = Label(ventana, text = "Basico 2")
texto.config(#para modificar el aspecto de los textos podemos usar propiedades como las siguientes, aunque hay mas
    fg="white",
    bg="black",
    padx=10,
    pady=20,
    font=("Console", 20),
    justify=RIGHT,
    width=30,
    height=4,
    cursor="arrow"

)
texto.pack(anchor=S)

texto = Label(ventana, text = "Basico 3")
texto.config(#para modificar el aspecto de los textos podemos usar propiedades como las siguientes, aunque hay mas
    fg="yellow",
    bg="blue",
    padx=10,
    pady=20,
    font=("Console", 20),
    width=30,
    height=4

)
texto.pack(anchor=N)

ventana.mainloop()