'''
Para crear una tupla con el metodo tuple()
se debe colocar entre corchetes dentro de los parentesis.
Las tuplas se pueden creear solo con los datos separados por
comas , 
'''
#Se puede crear como contructor de tupla
tupla = tuple(['Dato1', 'Dato2'])
print(tupla)

tupla_por_coma = 'dato1', 'dato2' #Se crean solo seprados por comas
print(tupla_por_coma)

thisTuple = ('apple',) #Para crear una tupla con un solo elemento, se debe colocar la , 
print(type(thisTuple))

thisTupleTow = ('apple', 'banana', True, 2)
print(type(thisTupleTow))