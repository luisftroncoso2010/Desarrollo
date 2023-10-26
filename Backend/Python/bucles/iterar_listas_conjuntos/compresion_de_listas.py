'''
Normalmente se recorre la lista de esta manera
'''
this_list = ['apple', 'banana', 'cherry']
new_list = list()

#Ciclo while
i = 0
while i < len(this_list):
    print(this_list[i])
    i+=1

#Por compresion de listas
[print(x) for x in this_list]

#con el ciclo for normal
for x in this_list:
    if 'a' in x:
        new_list.append(x)
print(new_list)

#Añadiendo datos por compresion de listas
#Solo aceptan los elementos que se valoran en true
new_list2 = [x for x in this_list if 'a' in x]
print(new_list2)

#Ejemplo: Guardar por compresion de listas en otra lista, exepto apple
new_list3 = [x for x in this_list if x !='apple']
print(new_list3)

#La condicion es opcional, se debe omitir 
new_list4 = [x for x in this_list]
print(new_list4)

#Se crea una lista en range()
new_list5 = [x for x in range(0, 10, 2)]
print(new_list5)

#El mismo ejemplo pero que solo llegue hasta 4
new_list6 = [x for x in range(10) if x < 6]
print(new_list6)

# Se peuden manipular los datos antes de que se impriman. 
# Por ejemplo cambiar a mayusculas
new_list7 = [x.upper() for x in this_list]
print(new_list7)

#Se pueden establecer todos los valores que se quieran. 
new_list8 = ['Hello' for x in this_list]
print(new_list8)

#Condiciones no com un filtro si no una forma de manejar 
# el resultado
new_list9 = [x if x!= 'apple' else 'orange' for x in this_list]
print(new_list9)