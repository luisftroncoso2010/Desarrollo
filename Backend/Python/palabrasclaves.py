import keyword
print(keyword.kwlist) # Palabras claves que no se pueden usar

x = 10
def funcion():
    return print(5)
funcion()
print(x)

a = list("letras")
print(a)

x = 0
while x < 3:
    print(x)
    x += 1
    
print('---Otro ejemplo parametros con diccionarios---')     
def varios(edad, año, **otros):
    #for i in otros.items():
        print(edad, año, otros)      
varios(26, 2023,  cinco = 5, dos = 2)

print('---Otro ejemplo con diccionarios que los devuelve como tuplas (Cuando se recorren)---') 
def parametros(edad, año, **otros):
    for i, y in otros.items():
        print(i, y)  
parametros(26, 2023, cinco = 5, dos = 2, tres = 3)

print('---Otro ejemplo con tuplas---') 
def parametros(edad, año, *otros):
    for i in otros:
        print(i)  

parametros(26, 2023, 5, 2, 3)
