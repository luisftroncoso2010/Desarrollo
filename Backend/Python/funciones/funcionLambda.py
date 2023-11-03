'''
Funcion lambda.
Es un forma de crear una funcion anonima y se asigna una variable
'''
numeros = [1, 22, 3, 4, 5, 6, 7, 8, 9, 10]

print('--Multiplicar un numero por 2 con lambda--')
multiplicarPorDos = lambda x : x*2 #Retorna automaticamente
print(multiplicarPorDos(5))

#Usando una funcion comun si es par uno
print('--Buscando numeros pares--')
def es_par(num):
    if (num% 2 == 0):
        return True
    else: 
        return False
print(es_par(6))

print('--Funcion filter--')
def paresList(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False
numerosParesList = (filter(paresList, numeros)) #Me duelve una lista con los numeros pares. Pro parametro primeero se le pasa el nombre de ka funcion y kuego el parametro de esa funcion
print(list(numerosParesList))

print('--Numeros pares pero con lambda--')
numerosParesLambda = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numerosParesLambda))