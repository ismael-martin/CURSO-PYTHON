"""
FOR 

for variable in elementoIterable:
    instrucciones

"""

contador = 0
resultado = 0

for contador in range(0,5):
    print("voy por el contador "+ str(contador))
    resultado += contador

print(f"El resutlado es {resultado}")

print("\n########### EJEMPLO 2 ###########")

numeroUsuario = int(input("De qué numero quieres la tabla?: "))

if numeroUsuario < 1:
    numeroUsuario = 1

print(f"TABLA DE MULTIPLICAR DEL NUMERO {numeroUsuario}")

for num in range(1,11):
    print(f"{numeroUsuario} x {num} = {numeroUsuario * num}")
    
print(f"TABLA DEL {numeroUsuario} TERMINADA")