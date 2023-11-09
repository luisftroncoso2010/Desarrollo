'''
Copiar una listas
'''
'''
Con el metodo copy()
'''
thisList = ['apple', 'banana', 'cherry']
myList = thisList.copy()
print(myList)


#Otra forma de copiar una listas es usando el metodo list()
myListDos = list(thisList)
print(myListDos)

'''
Unir dos listas. Con el simbolo mas +
'''
list_uno = ['a', 'b', 'c']
list_dos = [1, 2, 3]

print('---Se unen dos listas con el signo mas +---')
list_tres = list_uno + list_dos
print(list_tres)

'''
Unir dos listas desde un metodo.
Por ejemplo: for
'''
print('---Uniendos dos listas con un ciclo')
for x in list_dos:
    list_uno.append(x)
print(list_uno)

print('---Tambien se agregan lista usando el metodo extend')
list_uno.extend(list_dos)
print(list_uno)

