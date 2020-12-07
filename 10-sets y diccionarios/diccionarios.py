"""
Similar a una lista pero con la diferencia de que el indice del diccionario puede ser alfanumerico
en formato clave > valor
Parecido a un array asociativo
"""

persona = {
    "nombre": "Ismael",
    "apellidos": "Martín Gómez",
    "web": "www.pornhub.com"
}

print(persona)
print(persona["web"]) #para sacar el valor del indice que paso

#diccionario multidimensinal combinando listas con diccionatios

contactos = [
    {
        'nombre': 'Isma',
        'email': 'isma@isma.com'
    },
    {
        'nombre': 'Victor',
        'email': 'caca@isma.com'
    },
    {
        'nombre': 'Rubiuh',
        'email': 'flechipolla@isma.com'
    }
]

print(contactos[0]['nombre'])

print("LISTADO DE CONTACTOS")

for contacto in contactos:
    print(f"El nombre es: {contacto['nombre']}")
    print(f"El email es: {contacto['email']}")
    print("\n")
