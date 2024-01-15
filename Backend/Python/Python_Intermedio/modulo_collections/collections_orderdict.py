from collections import OrderedDict
'''orderedDict: Respeta el orden de inserccion de los datos'''


print('-- OrderedDict')


colours_ = OrderedDict([('Rojo', 180),
                        ('Amarillo', 70),
                        ('Azul', 160),
                        ('Verde', 750)])

'''Añadimos datos'''
# Asignando valores
colours_['Morado'] = (50, 80, 7, 70)
# Metodo update
colours_.update({'Rosado': 200, 'Blanco': 500})
# Metodo setdefault. Se añade solo si no existe
colours_.setdefault('Negro', 700)
# update como una lista de tuplas
colours_.update([('Gris', 400), ('Rosa', 400)])
# Método 'fromekeys()'
colours_.update(dict.fromkeys(['Rosa', 'Gris'], 600))
for key, value in colours_.items():
    print(f'{key} : {value}')
''' Cuando impirmimos el diccionario nos fijamos que
respeta el orden de inserccion '''


print('-- Recorrer un diccionadrio de manera normal')


colours = {'Rojo': 198, 'Verde': 170, 'Azul': 160}
# Recorremos el diccionario de manera normal
for key, value in colours.items():
    print(f'{key} : {value}')
