#Creando lista on list
lista = (['Ana', 22, 2023])
print(lista)
lista2 = ['Ana', 22, 2023]
print(lista2)
cadena = 'Hola'
resultado = len(cadena)
print(resultado)#Cuenta los elementos de la cadena
print(len(lista)) #Cuanta los elementos de lal sita
lista2.append('Andres')#Agregando un elemento elemento a la lista
lista2.insert(2, 24)#Agrega elementos a la lista indiandole el indice
#lista2[2] = 222 #Agrega elemento en la lista dependiendo el indice
lista2.extend([False, 'luis', 785])#Agega varios elementos a la lista
lista2.pop(4)#Elimina el elemento que querramos de la lista por indice
lista2.pop(-2)#Elimina el segundo elemnto en reverza
print(lista2)
lista.remove(22)#Remueve el elemento de la lista por valor
#del lista[0] #Elimina un valor por indice
print(lista2)
print(len(lista2))
listaNumerica = [4, True, 5, 7, False, 9]
listaNumerica.reverse()# Invierte los elementos de una lista 
listaNumerica.sort() #Ordena las listas de manera ascendent y solo resive datos numericos y Booleanos
listaNumerica.sort(reverse=True) #Los ordena de manera al contrario, desde el ultimo hacia el primero
index_ = listaNumerica.index(True)#Devuelve la psocion del elemento
print(listaNumerica)
print(index_) 
#print(lista2.clear())#Elimina todos los elementos de la lista
