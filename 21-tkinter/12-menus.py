from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

miMenu = Menu(ventana)
ventana.config(menu=miMenu)

archivo = Menu(miMenu, tearoff=0)
archivo.add_command(label="Nuevo")
archivo.add_command(label="Guardar")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_separator()
archivo.add_command(label="Exit", command=ventana.quit)

miMenu.add_cascade(label="Archivo", menu=archivo)
miMenu.add_command(label="Editar")
miMenu.add_command(label="Selección")






ventana.mainloop()