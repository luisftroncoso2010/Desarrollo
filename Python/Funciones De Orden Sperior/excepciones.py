""" Excepciones python """

print(' * Divicion entre 0: ')
def divicion(a, b):
    return a / b

try:
    resultado = divicion(1, 0)
except ZeroDivisionError:
    print('No se puede dividir entre 0')


print(' * Excepcion de numero entero:')

try:
    num = int('3a')
    print('No existe')
except NameError:
    print('La variable no existe')
except ValueError:
    print('El valor no es un numero')
else: 
    print('Bloque else: Solo se ejecuta si no a ocurrido una excepcion en el try')
finally:
    print('Bloque finally: Este se ejecuta siempre')
    

print(' * Crear nuestras propias excepciones: ')


class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return print(f'Error: {str(self.valor)}')

resultado = 30 
# Ejemplo de uso
try:
    if resultado > 20:
        raise MiError(33)
except MiError as e:
    print(e)
        