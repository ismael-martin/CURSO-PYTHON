from tkinter import *

ventana = Tk()
ventana.title("MARCOS - master en Python")
ventana.geometry("700x700")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="white",
    bd=5,
    relief="raised"
)
marco.pack(side=TOP, anchor=SW)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="grey",
    bd=5,
    relief="raised"
)
marco.pack(side=RIGHT, anchor=NE)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="lightblue",
    bd=5,
    relief="raised"
)
marco.pack(side=LEFT, anchor=SW)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief="raised"
)
marco.pack(side=LEFT, anchor=SW)


ventana.mainloop()