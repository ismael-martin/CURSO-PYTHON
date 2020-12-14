from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.pack()

def pruebas(nombre,apellidos, pais):
    return f"Hola {nombre} {apellidos}, te damos la bienvenida a {pais}"

texto = Label(ventana, text = pruebas(nombre="Ismael", apellidos="Martín", pais="España"))
#la llamada a la función pruebas() de la linea anterior funncionaria tambien si le pasamos los paramatreos desordenados usando keywords
texto.config(#para modificar el aspecto de los textos podemos usar propiedades como las siguientes, aunque hay mas
    fg="red",
    bg="orange",
    padx=10,
    pady=20,
    font=("Console", 20),
    justify=RIGHT,
    width=400,
    height=300,
    cursor="spider"

)
texto.pack(anchor=SE)

ventana.mainloop()