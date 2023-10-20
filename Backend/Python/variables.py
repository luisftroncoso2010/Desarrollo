print("--------------Listas---------------------")
lista = [99, True, "una lista"]
print(lista[1:])
print(lista[:2])
print(lista[:])
print(lista[::2])
lista2 = [4, 5]
print(lista.extend(lista2))

print("---------Tupla-----------------")
#Tupla
t = 1, 2, 3
print(type(t))

print("-----------Diccionario---------------")
#Diccionario
d1 = {
  "Nombre: ": "Sara",
  "Edad: ": 27,
  "Documento: ": 1003882
}
print(d1)
for x in d1:
    print(d1[x])
    

print('---Variable Tipo Complex---')
numero_complejo = 3 + 4j
print(numero_complejo)

