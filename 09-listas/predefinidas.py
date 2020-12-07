#metodos y funciones predefinidas para listas
peliculas = ["Batman","Spiderman","El señor de los anillos","The room"]
years = list(range(2020,2039))

#ordenar listas
print(peliculas)
peliculas.sort()
print(peliculas)

#añadir elementos
print(years)
years.append(2039)
print(years)

peliculas.insert(2,"Zombieland")
print(peliculas)

#eliminar elementos
peliculas.pop(2)
print(peliculas)
peliculas.remove('The room')
print(peliculas)

#dar la vuelta a la lista
print(years)
years.reverse()
print(years)

#buscar elementos
print("Batman" in peliculas) #devuelve True o False

#contar elementos
print(years)
print(len(years))

#cuantas veces aparece un elemento
print(years.count(2038))
years.append(2038)
print(years.count(2038))

#conseguir indice de la lista
print(years.index(2024))

#juntar dos listas
years.extend(peliculas)
print(years)