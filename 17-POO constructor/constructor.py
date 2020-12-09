#definir clase
class Coche:
    #crear atributos, son caracteristicas comunes a cada objeto, mediante el metodo constructor
    soyPublico = "Soy un atributo PUBLICO"
    __soyPrivado = "Soy un atributo PRIVADO"

    def __init__(self, color, marca, modelo, velocidad, caballos, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballos = caballos
        self.plazas = plazas

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
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setPlazas(self, plazas):
        self.plazas = plazas
    
    def getPlazas(self):
        return self.plazas
    
    def getInfo(self):
        info = "-------- INFO DEL COCHE --------"
        info += "\nMarca: "+ self.getMarca()
        info += "\nModelo: "+ self.getModelo()
        info += "\nColor: "+ self.getColor()
        info += "\nPlazas: "+ str(self.getPlazas())
        return info
    
    def getPrivado(self):
        return self.__soyPrivado
