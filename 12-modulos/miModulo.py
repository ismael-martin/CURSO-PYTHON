def holaMundo(nombre):
    return f"Hola {nombre}, que tal estás?"

def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2

    cadena = ""
    cadena += "Suma: "+ str(suma)
    cadena += "\nResta: "+ str(resta)
    if basicas == True:
        cadena += "\nMultiplicación: "+ str(multi)
        cadena += "\nDivisión: "+ str(divi)
    
    return cadena