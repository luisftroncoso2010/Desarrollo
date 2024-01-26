''' Busqueda binaria: Busca elementos especificos en una lsita ordenada
NOTA: Es mas eficiente que una busqueda normal.
'''
import random
import time  # Media de tiempo

print('--Busqueda Binaria--')


# Algoritmo busqueda binaria. (list, target)
def busqueda_binaria(lista, objetivo,
                     limite_inferiror=None, limite_superior=None):
    # Para le algoritmo de bsuqeda binaria,
    # la lista debe estar ordenada para que funcione
    # Si el valor por del inicio de la lista no se pasa se le asigna uno
    if limite_inferiror is None:
        # Se coloca 0, dado que el primer elemento su indice es 0(Cero)
        limite_inferiror = 0
    if limite_superior is None:
        # Se coloca -1 dado que el primer elemento del indice
        # es 0 hasta el ultimo elemento
        limite_superior = len(lista) - 1

    if limite_superior < limite_inferiror:
        return -1

    # Buscaramos el punto medio de la lista
    # Borra los decimales
    punto_medio = (limite_inferiror + limite_superior) // 2
    # Retornará el punto medio, dado que si el ojetivo esta ahi,
    # Devolvera el objetivo
    if lista[punto_medio] == objetivo:
        return punto_medio

    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo,
                                limite_inferiror, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo,
                                punto_medio+1, limite_superior)


print('--Algoritmo busqueda inocente--')


# Buscaremos un elemento en la lista y donde esta (lista, target)
def busqueda_ingenua(lista, objetivo):  # El objetivo se le dice Target
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1  # Se retorna un -1 ya que es un indice no valido


if __name__ == '__main__':
    # Esta es la lista
    # Crear una lista ordenada con 10000 números aleatorios
    tamaño = 100000
    conjunto_inicial = set()  # No habran elementos repetidos por ser set

    while len(conjunto_inicial) < tamaño:
        # Genera numeros enteros aleatorios
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el timepo en búsqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f'Tiempo de busqueda ingenua: {fin - inicio} segundos')

    # Mide el timepo de busqueda binaria
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f'Tiempo de busqueda binaria: {fin - inicio} segundos')
