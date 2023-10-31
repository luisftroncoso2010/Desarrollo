'''
Diccionarios anidados
'''

print('--Primer diccionario anidado--')
myFamily = {
    'Child1':{
        'name': 'Emil',
        'year': 2004
    },
    'Child2': {
      'Name': 'Tobias',
      'Year': 2007  
    },
    
    'Child3': {
        'Name': 'Luis',
        'Year': 2011    
    }        
}

print('--Acceder a los elementos en diccionarios enidados--')
print(myFamily['Child2']['Name'])

print('--Modificar valores de un diccionario anidado--')
myFamily['Child3']['Name'] = 'Andres'
print(myFamily['Child3']['Name'])

print('--Agregar nueevo a elemento a un diccionmario anidado--')
myFamily['Child4'] ={
    'Name': 'Leonardo',
    'Year': '1996'
}
print(myFamily)

print('--Iterar dicionarios anidados. Metodo items()--')
for clave, valor in myFamily.items():
    print(f'clave: {clave}')
    for subClave, subValor in valor.items():
        print(f'{subClave}: {subValor}')
        
print('--Eliminar elementos anidado o el diccionario--')
del myFamily['Child1']#Elimina el elemento seleccionado
print(myFamily)

