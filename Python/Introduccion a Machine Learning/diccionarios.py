# Creamos el diccionario
diciconario = {'nombre': 'victor', 'edad': 23}
print(diciconario)

# Filtrar por clave
print(diciconario['nombre'])
print(diciconario['edad'])

#Cambiar valor en diccionarios
datosPersonales = {'pais': 'italia', 'ciudad': 'roma'}
print(datosPersonales)
datosPersonales['ciudad'] = 'milan'
print(datosPersonales)

# Nuevo diccionario con dict
dict = {'jose': 18, 'david': 23, 'camila': 22}
dict.update({'raul': 22})
print(dict)
del dict['david']
print(dict)

# Combinar un diccionario con una lista
varones ={'jose': 18, 'david': 23}
mujeres = {'camila': 19, 'maria': 22}
estudiantes = list(dict.keys())  # Guardamos las llaves en una variable
print(estudiantes)
estudiantes.sort()  # Ordenamos la lista de las llaves
print(estudiantes)
for e in estudiantes:
    print(" : ".join((e, str(dict[e]))))
