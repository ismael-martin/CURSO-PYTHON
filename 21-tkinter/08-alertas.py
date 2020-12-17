from tkinter import *
from tkinter import messagebox as messagebox

def sacarAlerta():
    messagebox.showinfo("Alerta", "Tu gato se ha roto")

ventana = Tk()
ventana.config(bd=70)
Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

ventana.mainloop()