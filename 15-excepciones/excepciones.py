#mostrar errores personalizados y capturar posibles errores

try:
    nombre = input("Cual es tu nombre? ")

    if len(nombre)>1:
        nombre_usuario = "El nombre es "+ nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Todo ha ido correctamente")
finally:
    print("Fin de la iteración")

#manejar multiples excepciones
try:
    numero = int(input("Introduce un numero para elevarlo al cuadrado: "))
    print("El cuadrado de "+ str(numero) + " es: "+ str(numero*numero))
# except ValueError:
#     print("Mete un numero")
# except TypeError:
#     print("Debes convertir la cadena a entero")
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")

#Excepciones personalizadas
try:
    name = input("Introduce tu nombre: ")
    edad = int(input("Edad: "))
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(name)<=1:
        raise ValueError("El nombre no es correcto")
    else:
        print(f"Bienvenido {name} - {edad}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("existe un error")