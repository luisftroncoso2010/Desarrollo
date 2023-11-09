#Creamos una lsitas 
animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [10, 62, 12, 72]
diccionario = {'Nombre': 'Luis', 'Apellido': 'Troncoso'}

#Recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variables animal es igual a: {animal.capitalize()}')
    
#Recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#Recorres dos listas del mismo tamaña al mismo tiempo con la funcion zip (Resive mas parametros para iterar, CON EL MISMO TAMAÑO)
for numero, animal in zip(numeros, animales):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo listas 2 {animal}')
 
#Forma NO correcta de recorrer una lista    
for num in range(len(numeros)):
    print(f'Numero {numeros[num]}') #Solo recorre las posciones como tal
    
#Forma correcta de recorrer una lista con su indice y valor
'''
Las listas a diferencia de los diccionarios es que los 
diccionaerios tienen clave y valor, mientras que las listas
tienen indice y valor. Se filtarn de maenra distinta.
Los diccionarios con el metodo items() y las listas
y las listas con enumerate()

'''
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es {indice} y el valor de la tupla es {valor}')
    
#Recorrer clave/valor de un diccionario
for clave, valor in diccionario.items():
    print(f'Clave: {clave}, Valor: {valor}')


frutas = ["manzana", "plátano", "naranja", "uva"]
for indice, valor in enumerate(frutas):
    print(f"Índice {indice}: {valor}")

    
#Usando el else
for numero in numeros:
    print(f'Ejcuetando el ultimo bucle, del valor actual {numero}')
else:
    print(f'El bucle termino')