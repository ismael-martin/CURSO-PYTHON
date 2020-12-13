"""
tkinter es un modulo para crear interfaces graficas de usuario
"""
from tkinter import *
""" import os
directorio = os.listdir()
print(directorio) """
#crear la ventana raiz
ventana = Tk()

#Titulo de la ventana
ventana.title("Interfaz de la ventana")

#icono de la ventana
ventana.iconbitmap("/home/ismael/Documentos/PYTHON/CURSO PYTHON VICTOR ROBLES/21-tkinter/img/chrome.png")


#cambiar el tamaño de la ventana
ventana.geometry("750x450")

#bloequer tamaño de la ventana
ventana.resizable(0,0)
"""
son flags para bloquear el ancho y el alto
0 para bloquear
1 para desbloquear
"""

#arrancar y mostrar la ventana hasta que se cierra
ventana.mainloop()
