'''
Funciones definidas
'''
print('--Funciones por pocision--')
def frase(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos un {adjetivo}'
fraseresultante = frase('luis', 'Troncoso', 'capo')
print(fraseresultante)

print('--Funciones definidas--')
def fraseDos(nombre, apellido, adjetivo ='Capo'):
    return f'Hola {nombre} {apellido}, sos un {adjetivo}'
fraseresultanteDos = fraseDos('Luis', 'Troncoso')#No se le pasa el parametro a la funcion por que ya esta definida
print(fraseresultanteDos)

print('--Pasar parametros ASIGNADOS--')
def fraseTres(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, son un {adjetivo}'
fraseresultanteTres = fraseTres(apellido='Troncoso', adjetivo='capo', nombre='Luis')#Aca se le pasan los parametros desordenados pero ASIGNADOS 
print(fraseresultanteTres)