''' Exepcion '''
a = 4
while True:    
    b = int(input('Dale un valor de B: '))
    try:
        print(a / b) #Mandará una exepcion
    except: 
        print('Por favor cambiael valor de B')
    else: 
        print('Division correcta')
        break
    finally: print('Se ejecuneta cuneod termine')
    
#Ejemplo: generar una excepción con un mensaje personalizado
print('--Raise division personalizada--')
def dividir(a, b):
    if b == 0: 
        raise ValueError('No se puede dividir entre cero')
    return a / b
division = dividir(4, 2)
print(division)

#Generar una excepción generica sin mensaje
print('--Excepción sin mensaje--')
def mi_funcion(valor):
    if valor < 0:
        raise Exception("El valor no puede ser negativo")
    return valor * 2
miFuncion = mi_funcion(40)
print(miFuncion)

#Captura un excepción generada por raise
print('--Captura un excepción generada por raise--')
try:#Instancioamos la funcion y pasamos datos
    resultado = dividir(10, 2)#Pasamos los datos
except ValueError as ve:#Captamos la exepcion y traemmos de la funcion instanciada. Captura la el raise de sa funcion
    print(f'Error: {ve}')
else:
    print(f'resultado: {resultado}')

#Capturar u manejar una excepción genérica
print('--Capturar y manejar una excepcion genérica--')
try:
    resultado = mi_funcion(-4)
except Exception as e:
    print(f'Error: {e}')
else:
    print(f'Resultado: {resultado}')
    
print('--Uso del try y Except--')
n = 5
m = 0
try:
    p = n/m
except ZeroDivisionError:
    print('No se puede relizar la divicion')
else: print('Division exacta')

print('--Capturar Varias Excepciones--')
#Capturamos la excepcion 
try:
    #k = 5/0 #Aca entrará en ZeroDivision error
    d = 2 + "Hola"#Acá entrara en pproblemas de tipos
except ZeroDivisionError:
    print('No sse puede dividir entre 0')
except TypeError:
    print('Problemas de tipos!')    

print('--Capturar Varias Excepciones--')
#Capturamos la excepcion 
try:
    #k = 5/0 #Aca entrará en ZeroDivision error
    d = 2 + "Hola"#Acá entrara en pproblemas de tipos
except (ZeroDivisionError, TypeError) as e:
    print(f'No sse puede dividir entre 0 / Problemas de tipos! {e}')
    
print('--Excepsiones en el manejo de ficheros--')
#Creamos una excepsion para manear el archivo Read
try:
    with open('Fichero.txt') as file:#Este archivo no existe
        read_data = file.read()
except:
    #aca se entra si no pude ser abierto
    print('No se pude abrir:')

print('--Especificando el tipo de excepsion--')
#Se intetna abrir un fichero y se captura una posible excepción
try:
    with open('fichero.txt') as file:
        read_data = file.read()
except OSError as e:#para saber el erro hay que sabar lso tipos de errores
    print(f'OSError. no se pude abrir: {e}')
    


    





    