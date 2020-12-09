"""
PROGRAMA CON UNA LISTA CON 8 NUMERO ENTEROS
RECORRER LA LISTA PARA MOSTRARLA
ORDENARLA Y MOSTRARLA
MOSTRAR SU LONGITUD
BUSCAR ELEMENTOS QUE EL USUARIO PIDA POR TECLADO
"""

#defino una función para recorrerla
def recorrerLista(lista):
    cadena = ""
    print("## FUNCION RECORRER LISTA ##")
    for x in lista:
        cadena += str(x) + "\n"
    return cadena


#genero lista
lista = [8,5,2,3,7,2,6,1]

#recorro lista para mostrarla en pantalla
for list in lista:
    print(list)

print(recorrerLista(lista))

#ordeno la lista
print(lista)
lista.sort()
print(lista)

#muestro el tamaño de la lista
print(len(lista))

#buscar elemento dado
buscar = int(input("qué numero buscas? "))
resultado = lista.count(buscar)
if resultado > 0:
    print(buscar," aparece en la lista ",lista.count(buscar)," veces")
else:
    print(buscar," no esta en la lista")
