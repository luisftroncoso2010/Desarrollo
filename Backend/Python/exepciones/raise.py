''' Raise: Se utiliza para generar un excepcion en tu codigo de manera manueal'''
def dividir_numeros(dividendo, divisor):
    if divisor == 0:
        #El alue Error se usa cuando son dos tipos de datos correctos pero con valores incorrectos
        raise ValueError('El divisor no puede ser cero')
    return dividendo / divisor

#Creamo la excepsion
try:    
    resultado = dividir_numeros(4, 0)
except ValueError as e:
    print(f'Error: {e}')
else:
    print(f'Resultado: {resultado}')

#Ejemplo calcular raiz cuadrada 
print('--Ejemplo Raise. Raiz Cuadrada--')
def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError('No se puede calcular- Es iun numero negativo')
#Creamos la excepsion
try:
    result = calcular_raiz_cuadrada(-9)
except ValueError as e:
    print(f'Error: {e}')
else: print(f'El resultado es: {resultado}')

print('--Cadena de textos--')
def concatenar_strings(cadena1, cadena2):
    if not isinstance(cadena1, str) or not isinstance(cadena2, str):
        raise TypeError("Ambos arguemnteos deben de ser de tipo Strings")
    return cadena1 + cadena2

#Creamos la excepsion
try:
    resul = concatenar_strings("Hola", "EE")
except TypeError as e:
    print(f'Error: {e}')
else:
    print(f'Reseultado, cadenas unidas: {resul}')  
    
print('--Generar un error con un ripo de programa--')
def generar_error():
    r = 42 + '5'
    return r
#Creamos el bloque try catch
try:
    resulta = generar_error()
except TypeError as e:
    print(f'Se generar un error: {e}')
else: print(f'Resultado: {resulta}')