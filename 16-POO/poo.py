"""
CONCEPTOS
clases: codigo que crea el objeto
atributos: caracteristicas especificas del objeto que lo definen
metodos: funciones dentro del objeto que indica como se comporta el objeto
abstraccion: creación de multiples objetos difentes a partir de la misma clase
herencia: metodos y atributos que se importan de una clase superior (padre) a una clase inferior (hijo)
modularidad: división de la aplicación en partes mas pequeñas para ciertas tareas concretas
ocultación: metodos y atributos a los que sólamente se pueden acceder desde dentro de la clase

"""
#definir clase
class Coche:
    #crear atributos, son caracteristicas comunes a cada objeto
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F40"
    velocidad = 320
    caballos = 500
    plazas = 2

    #metodos, acciones que hacen los objetos
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    #getters y setters
    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, speed):
        self.velocidad = speed
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
    
#fin definición de clase
#crear objeto y acceso a atributos y metodos
coche1 = Coche()
print(coche1.marca) 

print(coche1.velocidad)
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar() #llamada a un metodo del objeto
print(coche1.getVelocidad())
coche1.setVelocidad(20)
print(coche1.getVelocidad())