'''
repetir de forma controlada el flujo de un codigo
'''
listaAnimales = ['Gato', 'Perro', 'Loro', 'Cocodrilo']
listaNumeros = [20, 10, 95, 100, 110, 50]

#Iteramos la lista para mostar los resultados
for i in listaAnimales:
    print(f'Ahora la variable animales vale: {i}')
    
#Multiplicar lista de numeros
for multiplicarNumero in listaNumeros:
    resultado = multiplicarNumero * 10
    print(resultado)
    
#Iteramos sobre dos listas
print('--Iterando dos listas. Funcion zip()--')
for listaUno, listaDos in zip(listaAnimales, listaNumeros):
    print(f'recorriendo lista Animalies {listaUno}')
    print(f'Recorriendo lista Numeros: {listaDos}')

#Iteramos usando la funcion range
print('--Funcion range--')
for numero in range(5, 10):
    print(f'Estos son los numeros del 5 al 10: {numero}')

#Forma NO CORRECTA DE ITERAR UNA LISTAS
print('--funcion len(). Contar posciones de una lista--')
for num in range(len(listaNumeros)):
    print(listaNumeros[num])
    
'''
NOTA: La funcion enumerate() funciona de tal manera 
en la tuplas y listas 
'''

#For correcta de iterar un lista
print('--Imprimir el Clave/valor de una lista--')
for i in enumerate(listaNumeros):
    indice = i[0]
    valor = i[1]
    print(f'El indice es: {indice} y el valor es: {valor}')

#Forma de sacar clave y valor
print('--Clave valor')
for clave, valor in enumerate(listaNumeros):
    print(f'Clave: {clave} valor: {valor}')

#usando el else 
print('--Usando el else--')
for numero in listaNumeros:
    print(f'Ejecutando el ultimo bucle {numero}')
else:
    print('El bucle termino')
        