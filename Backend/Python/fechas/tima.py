import time

#Obtener el tiempo actual en segundos desde la época
tiempo_actual = time.time()
print(f'Tiempo actual en segundos: {tiempo_actual}')

#Convertir tiempo en segundos a una estructura de tiempo
estructura_tiempo = time.gmtime(tiempo_actual)
#Esto da un  indicador de lo que imprime
print(f'Estructura de tiempo: {estructura_tiempo}')
