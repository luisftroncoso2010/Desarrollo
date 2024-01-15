from collections import Counter

'''Todos estos se almacenan segun su orden de ingreso'''
print('-- Cadena Uno')
cadenaUno = Counter('geeksforgeeks')
for i in cadenaUno.elements():
    print(i, end=' ')


print('\n-- Cadena de texto')
cadenaDos = Counter('qwerewqqwerrewq')
for i in cadenaDos.elements():
    print(i, end=' ')


print('\n-- Cadena de tres')
cadenaTres = Counter('bnvsrnmfvseyqwvfbyfdbhnbsdfbdfdvdfv')
for i in cadenaTres.elements():
    print(i, end=' ')


print('-- Uso de counter onclistas')


a = [13, 3, 4, 3, 5, 11, 12, 6, 7, 7]
x = Counter(a)
print(x)
# Iteramos sobre counter
for i in x.keys():  # Usamoa la funcion key() para iterar sobre las llaves
    print(i, ':', x[i])


x_keys = list(x.keys())
x_values = list(x.values())
print(x_keys)
print(x_values)


print('-- Uso del keys en diccionarios')


colours_ = {'Rojo': 180,
            'Amarillo': 70,
            'Azul': (160, 140, 754),
            'Verde': {750, 740, 800},
            'Naranja': (180, 178, 60),
            'Negro': [500, 400],
            'Blanco': 100,
            'Gris': 400}

x_colours_keys = list(colours_.keys())
print(x_colours_keys)
x_values_valores = list(colours_.values())
print(x_values_valores)
print(len(x_values_valores))


print('-- Elementos en una variedad de objetos --'.upper())
print('Example Number One')
# Crea
cadenaCuatro = Counter("geeksforgeeks")
for i in cadenaCuatro.elements():
    print(i, end=' ')

print('\nExample Number Two')
cadenaCinco = Counter({'geeks': 4, 'for': 1,
                       'gfg': 2, 'python': 3})
for i in cadenaCinco.elements():
    print(i, end=' ')

print('\nExample Number Tree')
cadenaSeis = Counter([1, 2, 21, 12, 2, 44, 5, 13, 15, 5, 19, 21, 5])
for i in cadenaSeis.elements():
    print(i, end=' ')

print('\nExample Number Four')
d = Counter(a=2, b=3, c=6, d=1, e=5)
for i in d.elements():
    print(i, end=' ')

'''NOTA: Counter imprime los valores en un itereble de tal manera que
los repite en le orden de inserccion'''

print('\n--Cuando se imprime directamente sin el ciclo')
cadenaSeis = Counter("geeksforgeeks")
print(cadenaSeis.elements())

print('-- Cuando se inicializa con valores negativos o ceros')
# al momento de imprmir de omiten los valores inferiores a uno
xx = Counter(a=2, x=3, b=3, z=1, y=5, c=0, d=-3)
for i in xx.elements():
    print("% s : % s" % (i, xx[i]), end='\n')
