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
    
    