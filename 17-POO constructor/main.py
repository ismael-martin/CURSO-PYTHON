"""
lo recomendable es crear el codigo de los objetos e importarlos en los ficheros que vamos a ejecutar para 
tener el código de nuestras aplicaciones lo mas organizado posible
"""
from constructor import Coche #llamo a la clase coche

coche1 = Coche("Azul","Kia","Picanto",140,80,4)#al instanciar el objeto le paso los atributos que quiero en el objeto al constructor
coche2 = Coche("Verde","Lamborghini","Huracan",320,600,2)
coche3 = Coche("Amarillo","Lamborghini","Murcielago",360,640,2)
coche4 = Coche("Gris","Nissan","GT-R",340,500,4)
coche5 = Coche("Negro","Audi","A4",280,320,5)
print(coche1.getInfo())
print(coche2.getInfo())
print(coche3.getInfo())
print(coche4.getInfo())
print(coche5.getInfo())

#detectar tipado
if type(coche3) == Coche:
    print("Es un objeto Coche")
else:
    print("No es un objeto")

coche3 = "String aleatorio"

if type(coche3) == Coche:
    print("Es un objeto Coche")
else:
    print("No es un objeto")

#visivilidad
print(coche4.soyPublico)
#print(coche4.__soyPrivado)
print(coche4.getPrivado())