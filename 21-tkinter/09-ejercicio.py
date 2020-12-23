"""
CALCULADORA:
    - 2 CAMPOS DE TEXTO
    - 4 BOTONES PARA OPERACIONES
    - MOSTRAR RESULTADO POR ALERTA
"""

from tkinter import *
from tkinter import messagebox as messagebox

calc = Tk()
calc.geometry("300x400")

##Genero las funciones de la calculadora
def suma(num1, num2):
    messagebox.showinfo("SUMA", f"La suma de {num1} y {num2} es {num1+num2}")

def resta(num1, num2):
    messagebox.showinfo("RESTA", f"La resta de {num1} menos {num2} es {num1-num2}")

def multi(num1, num2):
    messagebox.showinfo("MULTIPLICACIÓN", f"El producto de {num1} por {num2} es {num1*num2}")

def divi(num1, num2):
    messagebox.showinfo("DIVISIÓN", f"La división de {num1} entre {num2} es {num1/num2}")

def getNumeros(num1, num2, accion):
    input1 = IntVar()
    input2 = IntVar()
    input1.set(num1.get())
    input2.set(num2.get())

    
    if input1.get() >= 0 and input2.get() >= 0:
        if accion == "sumar":
            suma(input1.get(),input2.get())
        elif accion == "restar":
            resta(input1.get(),input2.get())
        elif accion == "multiplicar":
            multi(input1.get(),input2.get())
        elif accion == "dividir":
            divi(input1.get(),input2.get())
        


def salir():
    resultado = messagebox.askquestion("Salir", "Estas sseguro?")
    if resultado == "yes":
        calc.destroy()

#declaro las variables que voy a necesitar        
numero1 = IntVar()
numero2 = IntVar()

##encabezado
encabezado = Label(calc, text="CALCULADORA BÁSICA | Ismael Martín")
encabezado.config(
    padx=10,
    pady=10
)
encabezado.grid(row=0,column=0, columnspan=15, sticky=N)

#label para el campo (NUM1)
label = Label(calc, text="Primer numero")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

#campo de texto (NUM1)
campoTexto = Entry(calc, textvariable = numero1)
campoTexto.config(
    width=20,
    justify=RIGHT,
    state=NORMAL
)
campoTexto.grid(row=1, column=1 ,padx=5, pady=5)

#label para el campo (NUM2)
label = Label(calc, text="Segundo numero")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#campo de texto (NUM2)
campoTexto = Entry(calc, textvariable = numero2)
campoTexto.config(
    width=20,
    justify=RIGHT,
    state=NORMAL
)
campoTexto.grid(row=2, column=1 ,padx=5, pady=5)


Button(calc, text="SUMAR", command=lambda:getNumeros(numero1,numero2,"sumar")).grid(row=3,column=0)
Button(calc, text="RESTAR", command=lambda:getNumeros(numero1,numero2,"restar")).grid(row=3,column=1)
Button(calc, text="MULTIPLICAR", command=lambda:getNumeros(numero1,numero2,"multiplicar")).grid(row=4,column=0)
Button(calc, text="DIVIDIR", command=lambda:getNumeros(numero1,numero2,"dividir")).grid(row=4,column=1)
Label(calc).grid(row=5,column=0)
Button(calc, text="Salir", command=salir).grid(row=6,column=0,sticky=N)


calc.mainloop()