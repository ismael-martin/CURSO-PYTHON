import datetime
import hashlib
import conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario():
    def __init__(self,nombre,apellidos,email,contrasena):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = contrasena
    
    def registrar(self):
        fecha = datetime.datetime.now()
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.contrasena.encode('utf-8'))
        sql = "insert into usuarios values(null,%s,%s,%s,%s,%s)"
        usuarioNuevo = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha) 
        
        try:
            cursor.execute(sql, usuarioNuevo)  
            database.commit()

            result = [cursor.rowcount,self]
        except:
            result = [0,self]
        
        return result

    def identificar(self):
        #consulta para comprobar si existe el usuario
        sql = "select * from usuarios where email = %s and passwd = %s"

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.contrasena.encode('utf-8'))

        #datos para la consulta
        user = (self.email, cifrado.hexdigest())
        cursor.execute(sql,user)
        result = cursor.fetchone()
        return result