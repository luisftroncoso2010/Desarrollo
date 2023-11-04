'''
FUNCONES LAMBDA PYTHON
'''
print('--Suma de dos numeros eb lambda--')
suma = lambda a ,b: a + b
print(suma(2 , 4))

print('--Lambda para llamarla una sola ves')
multiplicacionLambda = (lambda a , b: a * b)(2, 4)
print(multiplicacionLambda)

print('--Lambda como entrada a una funcion normal--')
def mi_funcion(lambda_func):
    return lambda_func(2,4) #Aca se le pasan los parametros que se le piden a la funcion lambda

internaLambda = mi_funcion(lambda a, b: a + b)
print(internaLambda)

print('--Funcon con valor asignado--')
funLambSuma = (lambda a, b, c: a + b + c)(a=1, b=2, c=3)
funLambResta = (lambda a, b: a - b )(1, 2)
print(funLambSuma)
print(funLambResta)

print('--Resive tuplas por parametro--')
tuplasLamb = (lambda * args: sum(args))(1, 2, 3)#la tupla ya es lo ultimo
print(tuplasLamb)

print('--Funcion lambda para **Kawars--')
lambdaKwars = (lambda **kwars: sum(kwars.values()))(a = 1, b= 2, c=3)
print(lambdaKwars)

print('--Lambda para retornar mas de un valor--')
returnLambda = lambda a, b: (a, b)
print(returnLambda(3, 9))

print('--Ordenando lista por funcion lambda')
personas = [
    {"nombre": "Alice", "edad": 30},
    {"nombre": "Bob", "edad": 25},
    {"nombre": "Charlie", "edad": 35}
]

# Ordena la lista de personas por edad utilizando una función lambda
personas_ordenadas = sorted(personas, key=lambda x: x["edad"])

# Imprime la lista ordenada
print(personas_ordenadas)
