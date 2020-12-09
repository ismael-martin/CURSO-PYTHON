import clases
print("\nObjeto persona")
persona = clases.Persona()
persona.setNombre("Ismael")
persona.setApellidos("Martín")
persona.setAltura(178)
persona.setEdad(27)
print(persona.dormir())


#como funciona la herencia??
print("\nObjeto informatico")
informatico = clases.Informatico()
informatico.setNombre("Pepe")
informatico.setApellidos("Botella")
informatico.setAltura(150)
informatico.setEdad(78)
print(informatico.repararPC())
print(informatico.getLenguajes())