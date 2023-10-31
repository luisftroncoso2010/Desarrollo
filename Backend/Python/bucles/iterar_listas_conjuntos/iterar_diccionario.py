''' Iterar diccionarios'''

diccionarios = {
    'nombre': 'Lucas',
    'apellido': 'Dalto',
    'subs': 100000
}

#Recorre la clave, solo la clave del diccionario
for key in diccionarios:
    print(key.capitalize())#nos muestra la clave y convertimos cada clave su primera en mayusculas
    
#iterar el diccionario, clave/valor. Forma 1
for datos in diccionarios.items():
    key = datos[0]
    valor = datos[1]
    print(f'La llave es {key} y el valor es {datos}')
    
#iterar el diccionario, clave/valor. Forma 2
for llave, valor in diccionarios.items():
    print(f'La llave es {llave} y los valores son {valor}')

#Iterar una fruta    
frutas = ["manzana", "plátano", "naranja", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")




    