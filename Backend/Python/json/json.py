''' 
Json es una sintaxis para almacenar e intercambiar datos
Json es texto escrito con notación de objetos de javaScript
'''
import json
#Some Json
jsonn = '{"name": "Jhon", "age": 30, "city": "New York"}'
#Parse X:
y = json.loads(jsonn)
#The result is a python dictionary
print(f'La edad es : {y["age"]}')

'''Convertiremos a Json una objeto de python'''
objeto = {
    "name": "Jhon",
    "age": 30,
    "city": "New York"
}
#Convert int JSON
jison = json.dumps(objeto)#Con dumps se pueden convertir todo tipio de objetos en json
print(f'Esto es un json desde un diccionario: {jison}')

#Creamos un diccionarios con todos los valores, iterables para un json
xx = {
    "name": "Luis",
    "age": 40,
    "married": True,
    "divorced": False,
    "Children": ("Ann", "Billy"),
    "Pets": None,
    "Cars": [
        {"model": "BMW", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
#con indent facilita la lectura del resultado
print(json.dumps(xx, indent=6, separators=(". ", " = "), sort_keys=True))



