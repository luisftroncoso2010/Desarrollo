frutas = ['banana', 'manzana', 'ciruela', 'pera', 'naranja', 'granada', 'durazno']
cadena = 'Hola dalto'
numeros = [2, 5, 9]

print('---Muestra toda la lista---')
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')

#Cuando pase por granada se la salta
print('---Muestra todas menos granada---') 
for fruta in frutas:
    if fruta == 'granada':
        continue #si es la fruta granada salte
    print(f'Me voy a comer una {fruta}')
    
#Si se come la pera se cierra
print('---Se come la pera y se cierra---')
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
else: #Luego del break el else no se ejecuta
    print('Bucle finalizado')
    
#Recorrer una cadena de texto
print('---recorrer una cadena---')
for letra in cadena:
    print(letra)
    
#Agregar elementos a una listas
print('Agregar elementos a una lista')
numeros_duplicador = list()
for numero in numeros:
    numeros_duplicador.append(numero * 2)
print(f'La listas de numeros duplica dos es {numeros_duplicador}')
    
#Compresion de listas
print('---Compresion de listas---')
numeros_duplicados2 = [x*2 for x in numeros]
print(f'Esto se hizo por compresion de listas!. La lista de numeros duplicados es {numeros_duplicados2}')



