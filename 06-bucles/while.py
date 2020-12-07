"""
BUCLE WHILE

se ejecutará hasta que deje de cumplirse una condición

while condicion:
    instrucciones

"""
contador = 1
while contador <= 100:
    print(f"Estoy en el numero {contador}")
    contador += 1

print("----------------------------------------------")
contador = 1
texto = str(0)

while contador <= 100:
    texto = texto + ", " + str(contador)
    contador += 1
print(texto)

print("TABLA DE MULTIPLICAR CON WHILE")

numero = int(input("De qué numero quieres la tabla?: "))
contador = 1
if numero < 1:
    numero = 1

print(f"TABLA DEL {numero}")

while contador <= 10:
    print(f"{numero} * {contador} = {numero * contador}")
    contador += 1
else:
    print("TABLA TERMINADA")