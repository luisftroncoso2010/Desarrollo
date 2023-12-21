'''Depurando: Ayudar si tenemos un bug o fallo que necesitamos
resolver. Depurador PDB'''
# Con esto usamos pdb y tasar una linea de interrupcion
# import pdb; pdb.set_trace()


'''def haz_algo():
    # Aca se le asigna un break poin o puntos de ruptura
    pdb.set_trace()
    return "No quiero"'''


# print(haz_algo())


def sumar(list):
    sum = 0
    for item in list:
        sum += item
    return sum


''' Usando pdb:
* break _linea de interrupcion(Brak poin)
* continue: Sigue la ejecucion del programa
* next: Avanzando linea por linea
* continue: el programa sigue su curso normal
* list: Muesta el una lista donde esta detenidoel programa(Impimre 11 lineas)  
* p variable: Inspeccionamos variables'''


def agregar():
    digits = []
    for i in range(10):
        digits.append(i)
    sum(digits)


# Se debe agregar el metodo __name__ para que el debug lo toma la consola
if __name__ == '__main__':
    # Se le pasa pro parametro la lista
    sumar([1, 5, 10])
    agregar()
    
