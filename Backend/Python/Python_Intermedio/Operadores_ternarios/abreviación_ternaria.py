''' Forma acortada del operador ternario normal:
Esta versión es mas concisa se puede utilizar cuando
necesitas asignar un valor en funcion de una condición,
sin necesitada de la rama 'Si es falso'
'''


print('-- Version acortada del operador ternadrio')
# Solo trabaja Con valor True sin el valor de false, NO ES NECESARIO
x = -0.7
resultado = x if x > 0 else 0
print(resultado)  # Se basará en el resultado si es True si no imprime 0
print(True or 'Valor')  # Imprime True, dado trabaja con valores True
print(False or 'Valor')  # Imprime el valor


print('-- Evaludar vacios')
salida = None
msg = salida or "No se deolvio nada"
print(msg)  # Imprime el mensaje dado que salida esta vacio


print('-- Valores por defecto dinamicos')
'''NOTA: Recuerda que las abrevituras de los operadores
ternarios trabajan solo bajo valor de True '''


def mi_funcion(nombre_real, nombre_opcional=None):
    # La el primer bloque es true
    nombre_opcional = nombre_opcional or nombre_real
    print(nombre_opcional)


mi_funcion('Pelayo')  # Imprime pelayo, el valor del segundo parametro es vacio
mi_funcion('Covadonga', 'Cova')
