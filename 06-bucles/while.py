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