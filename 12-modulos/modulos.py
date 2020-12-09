"""
Los modulos son funcionalidades predefinidas listas para reutilizar
en python ya hay muchos modulos

podemos crear nuestros propios modulos, usar los que ya vienen en el lenguaje 
o usarlos de internet

tengo definidas dos funciones dentro de miModulo.py en esta misma carpeta, para usar ese modulo haré lo siguiente:
"""
#importo un modulo propio y ya puedo usar sus funciones
""" import miModulo

print(miModulo.holaMundo("Ismael"))

print(miModulo.calculadora(2,4,True)) """

#si solo quiero importar una función de miModulo:
#from miModulo import holaMundo

#tambien podemos importar las funciones de miModulo así
from miModulo import *
#from saca un aviso porque no estamos usando todas sus funciones
print(holaMundo("Ismael"))
print(calculadora(2,4,True))
