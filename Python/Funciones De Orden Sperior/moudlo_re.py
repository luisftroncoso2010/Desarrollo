import re


cadena = "Vamos a usar expresiones regulares"
print(re.search('usar', cadena))


'''Buscar texto con parametros tipo variables '''
print('     * Buscar cadena de texto en un formato: ')
textoBuscar = 'usar'
if re.search(textoBuscar, cadena) is not None:
    print('He encontrado el texto')
else:
    print('No he encontrado el texto')

print('     * Métodos start, end, span')
textoEncontrado = re.search(textoBuscar, cadena)
# Muestra el número de caracter donde ha encontrado el texto
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())


print('     * Expresiones regulares')
cadenaDos = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoFiltrar = "Python"
# Devuelve una lista con las coincidencias
print(re.findall(textoFiltrar, cadenaDos))
# Cuenta esa lista de cincidencias
print(len(re.findall(textoFiltrar, cadenaDos)))
