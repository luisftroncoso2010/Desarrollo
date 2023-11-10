'''
Cachin de funciones
'''
import time#Tiempo de ejecucion 
from functools import lru_cache
def esprimo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

#Tiempo de inicio
inicio = time.time()
#Llama a la funcion que deseas medir
resultado = esprimo(5)
#Registra el tiempo de finalzacion 
fin = time.time()
#Calcula la diferencia para obtener el tiempo de ejecución
tiempoDeejecucion = fin - inicio

print(f'El resultado es {resultado}')
print(f'Tiempo de ejecucion: {tiempoDeejecucion:0.5} segundos')


print('--Otro ejemplo--')
@lru_cache(maxsize=35)#Se alamacena en el cache para que corra mas rapid
def fib(n):
    if n<2:
        return n
    return fib(n-1)+(n-2)
start = time.perf_counter()
print([fib(n) for n in range(35)])
end = time.perf_counter()
print(f'Time: {end-start:0.5}')

print('--Caching con diccionarios--')
def es_primo_con_cache(num, _cache={}):
    if num not in _cache:
        _cache[num] = True
        for n in range(2, num):
            if num % n == 0:
                _cache[num] = False
                break
    return _cache[num]

tic = time.time()
es_primo_con_cache(25565479)
print(time.time() - tic)

tic = time.time()
es_primo_con_cache(25565479)
print(time.time() - tic)
