from tkinter import *
from tkinter import messagebox as messagebox

def sacarAlerta():
    messagebox.showinfo("Alerta", "Tu gato se ha roto")

def salir(nombre):
    resultado = messagebox.askquestion("Salir", "Estas sseguro?")
    if resultado == "yes":
        messagebox.showinfo("Hasta luego!", f"Nos vemos {nombre}")
        ventana.destroy()

ventana = Tk()
ventana.config(bd=70)
Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

Button(ventana, text="Salir", command=lambda: salir("Ismael")).pack()

ventana.mainloop()