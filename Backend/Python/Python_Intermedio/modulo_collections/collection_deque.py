from collections import deque


'''deque: Proporciona una cola con dos lados, lo que significa
que puedes añadir y eliminar elementos de los dos lados'''

print('-- deque, agregar elementos')


# Creamos el iterable
d = deque()
d.append('25')
d.append('14')
d.append('05')
d.append('10')
print(d)
print(f'Contamos los elementos de deque: {len(d)}')
print(f'Buscamos por indice. Izquierda a Derecha {d[0]}')
print(f'Buscamos por indice. Derecha a izquierda: {d[0]}')
'''NOTA: Cabe destacar que ambos usos muestra el elemento
eliminado de cada cola
* popleft, elemento de la izquierda (Inicio de cola)
* pop, elemento de la derecha (Fin de cola)'''
print(f'Uso de popleft: {d.popleft()} : {d}')
print(f'Pop: {d.pop()} : {d}')


print('-- Limitar la agregacion de elementos a cada cola')
# Creamos la lista con un maximo de 5 elementos
_deque = deque([54, 52, 9, 6, 'Luis'], maxlen=5)
print(_deque)
print(f'Lista: {_deque.append(57)} Add elements al final : {_deque}')
print(f"Lista: {_deque.appendleft('Inicio')} Add elements al inicio: {_deque}")
print(_deque)


print('-- Add datos')
'''NOTA: No se pueden agregar datos, mientras en maxlo'''
deque_ = deque([7, 9, 96, 35])
# Extendemos la lista deque
deque_.extend([1, 2, 3, 4, 50])
print(deque_)


print('-- De que con un range')
_deque_ = deque(range(4), maxlen=4)
_deque_.append('25')
_deque_.append('14')
_deque_.append('05')
_deque_.append('10')
print(_deque_)
