'''
Los conjuntos tambien se cran con una funcion set;
normalmente se crean con llaves
'''
#Creando conjunto con set
conjunto = set(['Dato1', 'Dato4' ])

#Metiendo un conjunto dentor de otro
conjunto1 = frozenset(['Dato1', 'Dato2']) #El conjunto se crea inmutable
conjunto2 = {conjunto1, 'Dato2'}
print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {2, 4, 8}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1 #Valida el resultado y mira si es un subconjuto 
print(resultado2)

#Varificamos si es un super conjunto
resultado3 = conjunto2.issuperset(conjunto1)
resultado4 = conjunto2 > conjunto1
print(resultado4)

#Verificar si hay algun numero en comun
resultado5 = conjunto2.isdisjoint(conjunto1)# Devuelve True cuando no hay ningun valor parecido
print(resultado5)