"""
CALCULADORA:
    - 2 CAMPOS DE TEXTO
    - 4 BOTONES PARA OPERACIONES
    - MOSTRAR RESULTADO POR ALERTA
    - LA CALCULADORA ES UN OBJETO
"""

from tkinter import *
from tkinter import messagebox as messagebox

class Calculadora():
    num1 = 0
    num2 = 0

    ##Genero las funciones de la calculadora
    def suma(self, num1, num2):
        messagebox.showinfo("SUMA", f"La suma de {self.num1} y {self.num2} es {self.num1+self.num2}")

    def resta(self, num1, num2):
        messagebox.showinfo("RESTA", f"La resta de {self.num1} menos {self.num2} es {self.num1-self.num2}")

    def multi(self, num1, num2):
        messagebox.showinfo("MULTIPLICACIÓN", f"El producto de {self.num1} por {self.num2} es {self.num1*self.num2}")

    def divi(self, num1, num2):
        messagebox.showinfo("DIVISIÓN", f"La división de {self.num1} entre {self.num2} es {self.num1/self.num2}")

    def getNumeros(self, num1, num2, accion):
        try:
            self.num1 = num1.get()
            self.num2 = num2.get()
                      
            if self.num1 >= 0 and self.num2 >= 0:
                if accion == "sumar":
                    self.suma(self.num1, self.num2)
                elif accion == "restar":
                    self.resta(self.num1, self.num2)
                elif accion == "multiplicar":
                    self.multi(self.num1, self.num2)
                elif accion == "dividir":
                    self.divi(self.num1, self.num2)
        except:
            messagebox.showerror("Error", "Los datos que has introducido no son correctos, por favor introduce enteros")  


    def salir(self):
        resultado = messagebox.askquestion("Salir", "Estas seguro?")
        if resultado == "yes":
            calc.destroy()


calc = Tk()
calc.title("Calculadora Básica")
calc.geometry("350x300")
calc.resizable(0,0)


#declaro las variables que voy a necesitar        
numero1 = IntVar()
numero2 = IntVar()

##encabezado
encabezado = Label(calc, text="CALCULADORA BÁSICA | Ismael Martín")
encabezado.config(
    padx=10,
    pady=10
)
encabezado.grid(row=0,column=0, columnspan=12, sticky=N)

#meto todo el contenido del formulario y los botones dentro del frame marco
marco = Frame(calc, width=250, height=250)
marco.config(
    padx=15,
    pady=15,

)
marco.grid(row=1,column=0)
#label para el campo (NUM1)
label = Label(marco, text="Primer numero")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

#campo de texto (NUM1)
campoTexto = Entry(marco, textvariable = numero1)
campoTexto.config(
    width=20,
    justify=RIGHT,
    state=NORMAL
)
campoTexto.grid(row=1, column=1 ,padx=5, pady=5)

#label para el campo (NUM2)
label = Label(marco, text="Segundo numero")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#campo de texto (NUM2)
campoTexto = Entry(marco, textvariable = numero2)
campoTexto.config(
    width=20,
    justify=RIGHT,
    state=NORMAL
)
campoTexto.grid(row=2, column=1 ,padx=5, pady=5) 

operaciones = Calculadora()

Button(marco, text="SUMAR", command=lambda:operaciones.getNumeros(numero1, numero2, "sumar")).grid(row=3,column=0)
Button(marco, text="RESTAR", command=lambda:operaciones.getNumeros(numero1, numero2, "restar")).grid(row=3,column=1)
Button(marco, text="MULTIPLICAR", command=lambda:operaciones.getNumeros(numero1, numero2, "multiplicar")).grid(row=4,column=0)
Button(marco, text="DIVIDIR", command=lambda:operaciones.getNumeros(numero1, numero2, "dividir")).grid(row=4,column=1)
Label(marco).grid(row=5,column=0)
Button(marco, text="Salir", command=operaciones.salir).grid(row=6,column=0,sticky=N)


calc.mainloop()