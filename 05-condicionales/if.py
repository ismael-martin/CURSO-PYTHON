#condicional IF

print("########### EJEMPLO 1 ############")

#color = "Rojo"
color = "Verde"

if color == "Rojo":
    print("Enhorabuena")
    print("El color es Rojo")
else:
    print(f"El color NO es Rojo, el color es {color}")

""" OPERADORES DE COMPARACIÓN
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""
print("########### EJEMPLO 2 ############")


year = 0#input("Introduce un año: ")

if int(year) >= 2020: #transformo year (string) a entero para comparar con otro numero
    print("Estamos en el futuro")
else:
    print("estamos en el pasado")

print("########### EJEMPLO 3 ############")

#ifs anidados
"""
nombre = input("Dime tu nombre: ")
ciudad = input("Dime tu ciudad: ")
continente = input("Dime tu continente: ")
MAYORIA_EDAD = 18
edad = int(input("Dime tu edad: "))

if edad >= MAYORIA_EDAD:
    print(f"{nombre} es mayor de edad!!")
    if continente.lower() != "europa":
        print("El usuario no es europeo")
    else:
        print(f"El usuario es europeo, vive en {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")
"""

print("########### EJEMPLO 4 ############")
#else if --> elif

dia = 0 # int(input("introduce el numero del día de la semana: "))
if dia > 0 and dia < 8:
    if dia == 1:
        print("es lunes")
    elif dia == 2:
        print("es martes")
    elif dia == 3:
        print("es miercoles")
    elif dia == 4:
        print("es jueves")
    elif dia == 5:
        print("es viernes")
    else:
        print("YA ES FIN DE SEMANA PUTO")
else:
    print("Te has equivocado con el numero de la semana")


print("########### EJEMPLO 5 ############")
#condiciones multiples
"""
OPERADORES LÓGICOS
and significa Y
or significa O
! significa negación
not significa NO
"""
EDAD_MINIMA = 18
EDAD_MAXIMA = 65
edad = 0#int(input("Introduce la edad: "))

if edad >= EDAD_MINIMA and edad <= EDAD_MAXIMA:
    print("Estás en edad de trabajar")
else:
    print("No deberias trabajar con tu edad")

print("########### EJEMPLO 6 ############")
#operador or
pais = "alemania" #input("introduce un pais: ").lower()

if pais == "mexico" or pais == "españa" or pais == "colombia":
    print("Es un pais de habla hispana")
else:
    print("NO es un pais de habla hispana")

print("########### EJEMPLO 7 ############")
#operador not
pais = "alemania" #input("introduce un pais: ").lower()

if not(pais == "mexico" or pais == "españa" or pais == "colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} Es un pais de habla hispana")

print("########### EJEMPLO 8 ############")
#operador !
pais = input("introduce un pais: ").lower()

if pais != "mexico" and pais != "españa" and pais != "colombia":
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} Es un pais de habla hispana")