import re


print('     * Comrpabamos si es cierto: ')
if re.match('.python', 'python'):
    print('Cierto')


print('     * Comparacion se caracteres, buscanto unas letras en una: ')
if re.match('.ython', 'python'):
    print('Cierto')
else:
    print('No es cierto')


print('     * Comprando varias expresiones irregulares con una: ')
if re.match('python|jython|cython', 'python'):
    print('Cierto')
else:
    print('No es cierto')


print('     * Buscando caracteres en especial: ')
if re.match('(p|j|c)ython', 'python'):
    print('Cierto')
else:
    print('No es cierto')


print('     * Clase de caracteres: ')
if re.match('[pjc]ython', 'python'):
    print('Cierto')
else:
    print('No es cierto')


print('     * Clase de caracteres: Numeros ')
if re.match('python[0-9]', 'python0'):
    print('Cierto')
else:
    print('No es cierto')


print('     * Todos los criterios: Todos los caracteres')
if re.match('[pjc]ython', 'python'):
    print('Cierto')
else:
    print('No es cierto')


print('     * No escapados: ')
if re.match('python[.,]', 'python,'):
    print('Cierto')
else:
    print('No es cierto')


print('     * Negacion: ')
if re.match('python[^0-9a-z]', 'python+'):
    print('Cierto')
else:
    print('No es cierto')
