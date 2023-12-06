import datetime

''' Fecha y hora. Una fecha en python no es un tipo de dato en si
misma, pero podemos importar el modulo datetime para trabajar
con fechas como objetos de fechas '''
#Importe el módulo de fecha y hora y muestre la fecha actual
fechaHora = datetime.datetime.now()
print(f'La fecha actual es: {fechaHora}')
print(f'El año actual es: {fechaHora.year}')
print(f"El dia de hoy es: {fechaHora.strftime('%A')}")
#Vamos a colocar una fecha exacta
fechaHoraAdaptada = datetime.datetime(2020, 5, 15, 6, 21, 10, 456)
print(f'Asignamos un valos de fecha y tiempoexacto: {fechaHoraAdaptada}')

#Formatear los objetos de fechas en cadenas legibles
fechaHoraAdaptadaa = datetime.datetime(2020, 5, 14, 6, 21, 10, 456)
print(fechaHoraAdaptadaa.strftime("%w"))


