from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

#para cargar imagenes en la ventana hacemos
foto = Image.open('./21-tkinter/img/mercedes.jpg')
render = ImageTk.PhotoImage(foto)

Label(ventana, image = render).pack(anchor=CENTER)


ventana.mainloop()