''' Busqueda binaria: Busca elementos especificos en una lsita ordenada
NOTA: Es mas eficiente que una busqueda normal.
'''
import random
import time #Media de tiempo

print('--Busqueda Binaria--')
#Algoritmo busqueda binaria. (list, target)
def busqueda_binaria(lista, objetivo, limite_inferiror = None, limite_superior = None):
#Para le algoritmo de bsuqeda binaria, la lista debe estar ordenada para que funcione
    if limite_inferiror is None:#Si el valor por del inicio de la lista no se pasa se le asigna uno
        limite_inferiror = 0 #Se coloca 0, dado que el primer elemento su indice es 0(Cero) 
    if limite_superior is None:
        limite_superior = len(lista) - 1#Se coloca -1 dado que el primer elemento del indice es 0 hasta el ultimo elemento
        
    if limite_superior < limite_inferiror:
        return -1
    
    #Buscaramos el punto medio de la lista
    punto_medio = (limite_inferiror + limite_superior) // 2 #Esto borra los decimales    
    #Retornará el punto medio, dado que si el ojetivo esta ahi, devolvera el objetivo
    if lista[punto_medio] == objetivo:
        return punto_medio
    
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferiror, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)
    

print('--Algoritmo busqueda inocente--')
#Buscaremos un elemento en la lista y donde esta (lista, target)
def busqueda_ingenua(lista, objetivo):#el objetivo se le dice Target
    for i in range(len(lista)):#
        if lista[i] == objetivo:
            return i
    return -1#Se retorna un -1 ya que es un indice no valido

if __name__ == '__main__':
    #esta es la lista
  #Crear una lista ordenada con 10000 números aleatorios
  tamaño = 30000
  conjunto_inicial = set()#No habran elementos repetidos por ser set
  
  while len(conjunto_inicial) < tamaño:
      conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))#genera numeros enteros aleatorios   
    
  lista_ordenada = sorted(list(conjunto_inicial))
  
  #Medir el timepo en búsqueda ingenua
  inicio = time.time()
  for objetivo in lista_ordenada:
      busqueda_ingenua(lista_ordenada, objetivo)
  fin = time.time()
  print(f'Tiempo de busqueda ingenua: {fin - inicio} segundos')
  
  #Medi el timepo de busqueda binaria
  inicio = time.time()
  for objetivo in lista_ordenada:
      busqueda_binaria(lista_ordenada, objetivo)
  fin = time.time()
  print(f'Tiempo de busqueda binaria: {fin - inicio} segundos')
  
  
  
    
    



