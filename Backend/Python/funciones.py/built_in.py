'''
Funciones built_in
'''
myList = list([4,20,10,50,80,711])
#Econtrando el numero mayor de una lista
print('--Numero mas alto--')
numero_mas_alto = max(myList)
print(numero_mas_alto)

print('--Numero mas bajo--')
numero_mas_bajo = min(myList)
print(numero_mas_bajo)

print('--Redondear numeros--')
numero = round(12.457821, 2)#Este numero nos da numeros decimales
print(numero)

print('--Retorno de valores verdaderos o falso')
#Retorna false, cuando se le pase nada, vacio o False. Todo lo diferente a esto es verdadero
resultBool = bool(2)
print(resultBool)

print('--Retorna True si todos los valores son verdaderos--')
#Retorna True ti todos los valoresd son verdaderos de un iterable
resulAll = all([True, 123, 1])
print(resulAll)

print('--La suma de un itetrable')

sumIterable = sum(myList)
print(sumIterable)