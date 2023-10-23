#Crean variables nuevas por ejemplo de una tupla.
datos_en_tupla = ('Lucas', 'Dalto', 100)
datos_en_lista = ['Lucas', 'Dalto', 100]
''' Para que funcione el desempaquetado se debe 
colocar el mismo numero de variables correspondiente
al mismo numero de datos en la tupla. 
Se pueden contar con la funcion (len())
'''
print(f'Numero de datos de la tupla {len(datos_en_tupla)}')
nombre, apellidos, suscriptores = datos_en_tupla
print(nombre, apellidos, suscriptores)
print(f'---Desempaquetado en lista---')
nombre, apellidos, suscriptores = datos_en_lista
print(nombre, apellidos, suscriptores)
