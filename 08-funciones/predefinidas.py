#FUNCIONES PREDEFINIDAS
"""
print() imprime por pantalla
print(type(variable)) devuelve el tipo de variable
isinstance(variable,tipoVariable) devuelve True o False


"""
nombre = "Ismael Martin"
print(nombre)
print(type(nombre))

comprobar = isinstance(nombre, str)
if comprobar:
    print("la variable es una string")
else:
    print("NO es una string")

if not isinstance(nombre, float):
    print("No es un float")

#limpiar espacios
texto = "     hola  que   tal? como t   e llaMAS"
print(texto)
print(texto.strip())

#eliminar variables
year = 2020
print(year)
del year

#comprobar variables vacias
cadena = "  ff  "
if len(cadena) > 0:
    print("la variable no esta vacia",(len(cadena)))
else:
    print("Esto está vacio")

#encontrar caracteres
frase = "la vida es bella"
print(frase.find("vida"))

#reemplazar palabras en un string
nueva_frase = frase.replace("vida", "coca")
print(frase)
print(nueva_frase)

#mayusculas y minusculas
print(frase.upper())
print(frase.lower())
print(frase.capitalize())