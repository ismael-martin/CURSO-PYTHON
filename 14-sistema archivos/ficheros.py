from io import open
import pathlib
import shutil #para copiar, renombrar, eliminar archivos...

#abrir fichero
"""
Tengo que tener en cuenta desde dónde ejecuto el script, mi ruta absoluta es ~/Documentos/PYTHON/CURSO PYTHON,
es por eso que a ruta le tengo que pasar "/14-sistema archivos" para que guarde fichero-texto.txt dentro de esa carpeta
"""
ruta = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-texto.txt"
archivo = open(ruta, "a+")

#escribir dentro del archivo
archivo.write("***********SOY UN TEXTO ESCRITO DESDE PYTHON*****************\n")

#cerrar fichero
archivo.close()

#abrir fichero nuevamente
ruta = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

#leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elem in lista:
    print(elem)


#copiar
rutaOrigen = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-texto.txt"
rutaDestino = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-COPIADO.txt"
shutil.copyfile(rutaOrigen, rutaDestino)

#renombrar y mover archivos
rutaOrigen = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-texto.txt"
rutaDestino = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-RENOMBRADO.txt"
shutil.move(rutaOrigen,rutaDestino)

#eliminar archivo
import os
otraRuta = str(pathlib.Path().absolute()) + "/14-sistema archivos/fichero-RENOMBRADO.txt"
os.remove(otraRuta)

#comprobar si existe
print(os.path.isfile(os.path.abspath("./14-sistema archivos/fichero-RENOMBRADO.txt"))) #imprime False porque lo acabo de borrar
print(os.path.isfile(os.path.abspath("./14-sistema archivos/fichero-NUEVO.txt"))) #imprime True porque existe en dentro de la ruta