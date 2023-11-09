'''
Ordenar listas con el metodo short.
Ordenara la lista de forma alfanumerica 
ascendente de forma predeterminada
'''
#Ordena la lista de manera alfabeticamente
thisList = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thisList.sort()
print(thisList)

#Ordena las listas de manera numericamente ascendente
thisList2 = [100, 50, 68, 40, 90, 101]
thisList2.sort()
print(thisList2)

"""
Para ordenar de manera descendente se debe usar el
el argumento de la palabra clave reverse = True:
"""
#Ejemplo de manera descendente; desde la Z hasta A
thisList.sort(reverse=True)
print(thisList)

#Ahora ordenamos de manera descendente los numeros, de mayor a menor 
thisList2.sort(reverse=True)
print(thisList2)
