'''try. Se coloca una excepcion'''


print('-- Excepciones')


try:
    file = open('text.txt', 'rb')
except IOError as e:
    print(f'Ocurrió un IOError {e.args[-1]}')


print('-- Manejando múltiples excepciones')


try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print(f'Ocurrió un error: {e.args[-1]}')


print('-- Manejar varias excepciones de manera individual')


try:
    file = open('test.txt', 'rb')
except EOFError:
    print('Ocurrió un EOError')
except IOError:
    print('Ocurrió un IOError')


'''NOTA: Tambien existe una menera para manejar todas las
opciones ne un solo bloque'''


print('-- Bloque finally')


try:
    print('No habrá excepcion, se ejecuta el bloque else')
except EOFError:
    print('Ocurrió un EOError')
except IOError:
    print('Ocurrió un IOError')
else:
    print('Sei estas aca es por que no hay excepcion')
finally:
    print('Se entra aca haya o no haya excepción')
