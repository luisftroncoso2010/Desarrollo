'''
Uni dos conjuntos con los metodos union() devuelve un 
metodo un nuevo conjunto que contine ambos conjuntos o el
metodo update() metodo que inserta todos los elementos de
un conjunto en otro
'''
print('--Metodo union()--')
setUno = {'a', 'b', 'c'}
setDos = {1, 2, 3}
print(setUno.union(setDos)) #Los devuelve al azar y desordenado
'''
Tanto union() como update() excluiran elementos desordenados
'''
print('--Metodo Update--')
setTres = {10, 20, 30, 40}
setCuatro = {'Luis', 'Rangel', 'Fernando'}
setUno.update(setDos) #No se puede mantener en una variable por que lo devolvera vacio, ya que esto solo actualiza
print(setUno)#Al impirmi el Update() excluira cualquier elemento repetido

print('--En una unave variable manteno los elementos existentes--')
setX = {'ingeniero', 'Licenciado', 'Profesor'}
setY = {'google', 'Licenciado', 'Profesor'}
setX.intersection_update(setY)#Mantiene los elementos que estan en ambos sets
print(setX)#NO ELIMINARA LOS DUPLICADOS

print('--Conserva todo pero no los duplicados--')
setP = {'ingeniero', 'Quimico', 'Licenciado', 'Profesor'}
setQ = {'google', 'ACEB', 'Licenciado', 'Profesor'}
#Me traera todos los elemntos que estan A y no en B que no sean REPETIDOS
setQ.difference_update(setP)
print(setQ)

print('--symmetric_difference--')
setWW = {'apple', 'banana', 'cherry', 'mango'}
setAA = {'google', 'microsoft', 'apple', 'samsumg'}
asasa = setWW.symmetric_difference(setAA)
print(asasa)#Si los valores estan en ambos, no trae ninguno