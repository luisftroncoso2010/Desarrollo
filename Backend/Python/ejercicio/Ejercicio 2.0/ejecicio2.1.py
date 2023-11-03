#Falto el profe y los pibes van armar la clase.
'''
Hoy falto el profesor de clase y los chicos se las 
para armar la suya propia. 
Uno de los alumnos va ser el profesor y el otro uno asistentes
A) Pedir el nombre y la edad de los compañeror que vinieros
hoy a clases y ordenar de mayor a menor
B) El mayor de los dos es e lel profesor o es el alumno
'''
#Falto el profe y los pibes van armar la clase

#Pedir el nombre y la edad los comprañeros que vnieron a clases
def obtenter_compañeros(cantidad_de_lista):
    lista = list()
    for i in range(cantidad_de_lista):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        compañero = (nombre, edad)
        lista.append(compañero)
    lista.sort(key=lambda x:x[1])
    asistente = lista[0][0]
    profesor = lista[-1][0]
    for tupla in lista:
        nombreCom, edadCom = tupla
        print(f'El compañero es: {nombreCom} y la edad es: {edadCom}')
    
    return asistente, profesor

asistente, profesor = (obtenter_compañeros(3))
print(f'El pofesor es: {profesor} y su asistente es {asistente}')