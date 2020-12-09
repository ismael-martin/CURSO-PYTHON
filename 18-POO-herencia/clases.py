#HERENCIA es la posibilidad de compartir atributos y metodos entre clases relacionadas

class Persona:#clase padre
    def __init__(self, nombre, apellidos, edad, altura):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.altura = altura
    
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getEdad(self):
        return self.edad

    def getAltura(self):
        return self.altura

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setEdad(self, edad):
        self.edad = edad

    def setAltura(self, altura):
        self.altura = altura

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "EStoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona): #clase hijo
    """
    lenguajes
    experiencia
    """
    def __init__(self,nombre,apellidos,edad,altura):#si uso super aqui necesito que me pasen los atributos para mandarlos al constructor padre
        super().__init__(nombre,apellidos,edad,altura) #super hace la llamada al constructor de la clase padre para que se ejecute al crear un objeto hijo
        self.lenguajes = ["HTML","CSS","JavaScript","PHP"]
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def setLenguajes(self, lenguaje):
        self.lenguajes.append(lenguaje)
    
    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "Estoy reparando un PC"
