import calendar

#Crear un objeto calendario
calendario = calendar.TextCalendar(calendar.SUNDAY)

#Imprimir el calendario
calendario_enero = calendario.formatmonth(2024, 1)
calendario_febrero = calendario.formatmonth(2024, 2)
print(calendario_enero)
print(calendario_febrero)