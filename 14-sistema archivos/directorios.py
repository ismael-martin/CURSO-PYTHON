import os, shutil

#crear carpeta
if not os.path.isdir("./14-sistema archivos/carpeta"):#compruebo si existe la carpeta y la creo
    os.mkdir("./14-sistema archivos/carpeta")
else:
    print("La carpeta ya existe")

#borrar carpeta
if os.path.isdir("./14-sistema archivos/mi_carpeta2"):#compruebo si existe la carpeta y la borro
    os.rmdir("./14-sistema archivos/mi_carpeta2")
else:
    print("La carpeta ya no existe")

#copiar carpeta
rutaRelativa = "./14-sistema archivos/mi_carpeta"
rutaNueva = "./14-sistema archivos/mi_carpeta_COPIADA"
shutil.copytree(rutaRelativa, rutaNueva)

#mostrar contenido de la carpeta
contenido = os.listdir("./14-sistema archivos/mi_carpeta")
print(contenido)#contenido es una lista
for fichero in contenido:
    print(f"fichero: {fichero}")