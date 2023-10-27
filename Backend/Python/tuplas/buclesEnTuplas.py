'''
Recorrer los elementos de una tupla usando bubles
for y while
'''
thisTuple = ('apple', 'banana', 'cherry')
print('---Muestra los valores de la tupla. Bucle while')
for x in thisTuple:
    print(x)

print('---Recorrer el indice de una tupla---')
#Esto hace los mismo que lo anterior pero NO es lo recomendado
for i in range(len(thisTuple)):
    print(thisTuple[i])
    
    
