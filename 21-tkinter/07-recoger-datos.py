from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd = 50
)

def getDato():
    result.set(dato.get())
    
    if len(result.get()) >=1:
        textoRecofigo = Label(ventana, textvariable=result)
        textoRecofigo.config(
            bg="green",
            fg="white"
        )
        textoRecofigo.pack(anchor=NW)


dato = StringVar()
result = StringVar()

Label(ventana, text="Mete un texto:").pack(anchor=NW)
Entry(ventana, textvariable = dato).pack(anchor=NW)


Label(ventana, text="Dato recogido:").pack(anchor=NW)



Button(ventana, text="Mostrar dato", command= getDato).pack(anchor=NW)


ventana.mainloop()