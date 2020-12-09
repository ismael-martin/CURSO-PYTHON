import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.day)
#en la documentación de python aparece todas las opciones de formateo de fechas
fechaPersonalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fechaPersonalizada)

tiempoUnix = datetime.datetime.now().timestamp()
print(tiempoUnix)