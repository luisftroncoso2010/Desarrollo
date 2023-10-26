#Creamos una lsitas 
animales ={'gato', 'perro', 'loro', 'cocodrilo'}
numeros = {10, 62, 12, 72}
diccionario = {'Nombre': 'Luis', 'Apellido': 'Troncoso'}

#Recorriendo la conjunto animales
for animal in animales:
    print(f'Ahora la variables animal es igual a: {animal.capitalize()}')
    
#Recorriendo la conjunto numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#Recorres dos conjuntos del mismo tamaña al mismo tiempo con la funcion zip (Resive mas parametros para iterar, CON EL MISMO TAMAÑO)
for numero, animal in zip(numeros, animales):
    print(f'Recorriendo conjunto 1: {numero}')
    print(f'Recorriendo conjuntos 2 {animal}')
 
   
#Forma correcta de recorrer una conjunto con su indice y valor
'''
Las conjuntos a diferencia de los diccionarios es que los 
diccionaerios tienen clave y valor, mientras que las conjuntos
tienen indice y valor. Se filtarn de maenra distinta.
Los diccionarios con el metodo items() y las conjuntos
y las conjuntos con enumerate()

'''
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es {indice}y el valor de la tupla es {valor}')
    
#Recorrer clave/valor de un diccionario
for clave, valor in diccionario.items():
    print(f'Clave: {clave}, Valor: {valor}')
    
#Usando el else
for numero in numeros:
    print(f'Ejcuetando el ultimo bucle, del valor actual {numero}')
else:
    print(f'El bucle termino')