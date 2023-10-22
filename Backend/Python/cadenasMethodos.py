import time
#Longitud de cadena
a = 'Hello, world'
b = '¿Como estas?'
age = 37
name = 'Luis'
print(f'Longitud de cadena {len(a)}')
print(f'Precision de poscion en cadena {a[1]}')
print('Hello' in a)
print('hola' not in a)
print(f'Me trae una rebanada del texto{a[2:5]}')
print(f'corta desde un principio {a[:5]}')
print(f'Corta desde el inicial hasta el final {a[2:]}')
print(f'Indexacion negativa {a[-5:-2]}')
print('Separa toda las letras una debajo de la otra')
for x in 'Banana':
    print(x)
print(f'Convierte las cadenas en mayusculas {a.upper()}')
print(f'Convierte las cadenas en miniscula {a.lower()}')
print(f'Elimina cualqueier espacio en blanco {a.strip()}')
print(f'Remplazar cadenas (Palabras) {a.replace("Hello","Hola")}')
print(f'Divide las cadenas en subcadenas donde encuentre la coincidencia {a.split(",")}')
print(f'Concatenar cadenas {a + b}')
print(f'Concatenar cadenas {a} {b}')
print(f'{a} tengo {age} años')
txt = 'My name es {}, and I am {} años'
print(txt.format(name ,age))
print(f'Caracteres de escape'.upper())
print('Hello\tmedellin')#Da un espacio como si fuera un tabulador
print('Hello\n medellin')#Salto de linea 
print('Hello\rWorld!')

for i in range(5):
    print(f'Progreso: {i + 1} de 5', end='\r') #Remplaza le existente por uno nuevo texto
    time.sleep(1)# 
print('It\'s alright')
print('Hello \b World!') #Quita los espacios
cadena1 = 'Hola soy luis fernando'.capitalize() #Convierte la primera en mayuscula 
cadena2 = "Bienvenido luis"
numeros = '123456';
#print(dir(cadena1)) #Muestratodo lo que se pudeda hacer que contenta esa variable
print(cadena2.find('d'))#Busca una cadena en una cadena. La cincidencia y me da la poscion
print(cadena2.index('d'))# Si no hay coincidencias lanza una ecepsion
print(numeros.isnumeric()) #Resivela cadena solo si es numerica
print(cadena2.isalpha()) #Devuelve true si solo hay caracteres alfabeticos (Cuenta los espacios y todo)
print(cadena2.count('b')) #Devuelves el numero de coincidencias
print(len(cadena2))#Aumenta los caracteres que hay
print(cadena2.startswith('Bi'))#Verifica con que empieza la cadena, con que caracter
print(cadena2.endswith('is'))#Verifia con que finaliza la cadena

