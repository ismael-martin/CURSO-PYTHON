#pruebas con variables

#creación de variables y asignación de valores
texto = "Master en Python"
print(texto)

texto2 = "con Victor Robles"
print(texto2)

numero = 45
print(numero)

numero = 6.7 #reasignación de valores
print(numero)

print("-------------------------------------------")
#concatenación
nombre = "Ismael"
apellidos = "Martín"

print(nombre + " " + apellidos) #forma 1 de concatenar variables
print(nombre,apellidos) #forma 2 de concatenar variables, esta forma funciona como una función a la que le pasamos variables sin mas
print(f"{nombre} {apellidos}") #forma 3 de concatenar variables
print("Hola me llamo {} {}".format(nombre,apellidos)) #forma 4 de concatenar variables, format sirve para indicarle a print el lugar donde colocar los datos que le pasamos




