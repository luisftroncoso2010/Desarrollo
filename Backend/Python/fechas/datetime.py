from datetime import datetime, date, time, timedelta

#Obtener la fecha y la hora actual
fecha_hora_actual = datetime.now()
print(f'La fecha y la hora actual es: {fecha_hora_actual}')

#Obtener solo la fecha actual. Años, mes, dia
fecha_actual = date.today()
print(f'Fecha actual: {fecha_actual}')

#Obtener solo la hora actual. Hora, minutos, segundos, milisegundos
hora_actual = datetime.now().time()
print(f'Hora actual: {hora_actual}')

#Fecha especificada
fecha_personalizada = date(2021, 1, 15)
print(f'Fecha especificada: {fecha_personalizada}')

#Operaciones con fechas y horas
fecha_futura = fecha_actual + timedelta(days=7)
print(f'Fecha dentro de una semna: {fecha_futura}')