"""
tkinter es un modulo para crear interfaces graficas de usuario
"""
from tkinter import *
import os.path



class Programa:
    def __init__(self):
        self.titulo = "Master en Python de Ismael Martín"
        self.icon = "@./21-tkinter/img/favicon.xbm"
        self.icon_alt = ""
        self.size = "770x400"
        self.resizable = True
        self.ventana = Tk()
    
    def cargar(self):
        #crear la ventana raiz
        #Titulo de la ventana
        self.ventana.title(self.titulo)
        ruta_icono = os.path.abspath(self.icon)
        #icono de la ventana
        self.ventana.iconbitmap(self.icon)
        #NO SE EXPLICA EN EL CURSO: en linux hay que poner @ segudo de la ruta (absoluta o relativa) del icono
        #e iconbitmap solo reconoce archivos con formato xbm, mas adelante buscaré la forma de incluir cualquier icono en cualquier formato

        #mostrar texto en la ventana
        texto = Label(self.ventana, text = ruta_icono)
        texto.pack()

        #cambiar el tamaño de la ventana
        self.ventana.geometry(self.size)

        #bloequer tamaño de la ventana
        if self.resizable:
            self.ventana.resizable(1,1)
        else:
            self.ventana.resizable(0,0)
        #los paramoretros del metodo resizable son (ancho, alto)
        """
        son flags para bloquear el ancho y el alto
        0 para bloquear
        1 para desbloquear
        """
    def mostrarVentana(self):
        #arrancar y mostrar la ventana hasta que se cierra
        self.ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

programa = Programa()
programa.cargar()
programa.addTexto("hola")
programa.addTexto("que tal")
programa.addTexto("me llamo ismael")
programa.mostrarVentana()