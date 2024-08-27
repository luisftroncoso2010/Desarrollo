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


print('     * Metacaracteres: ')
listaNombres = ['Ana Gómez', 'María Martín', 'Sandra López',
                'Santiago Martín', 'Mañana', 'España',
                'Nano', 'Camion', 'Camión']
print(' - Buscamos los que inicien con una palabra: ')

for elemento in listaNombres:
    # Filtramos todo lo que comienza con cierto caracter
    if re.findall('^Sandra', elemento):
        print(elemento)

print('- Buscamos palabra al finalizar texto:')

for elemento in listaNombres:
    # Filtramos todo lo que finaliza con cierto caracter
    if re.findall('Martín$', elemento):
        print(elemento)

print(' - Buscamos una ñ en el epacio: ')
for elemento in listaNombres:
    if re.findall('[ñ]', elemento):
        print(elemento)

print('- Buscamos por sexo o plural: ')
listaSexos = ['Hombres', 'Mujeres', 'Niños', 'Niñas', 'Homosexuales']
for elemento in listaSexos:
    if re.findall('Niñ[oa]s', elemento):
        print(elemento)

print('- Buscamos por tilde')
for elemento in listaNombres:
    if re.findall('Cami[oó]n', elemento):
        print(elemento)

print('     * RANGOS:')

listaNombresDos = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']

for elemento in listaNombres:
    # Ranfos entre la o y t dentro de sus letras
    if re.findall('^[o-t]', elemento):
        print(elemento)

print('- Rangos al final: ')
for elemento in listaNombres:
    # Ranfos entre la o y t al final de sus letras
    if re.findall('^[o-t]$', elemento):
        print(elemento)

print('- Rangos al final')
listaCiudades = ['Ma1', 'Se1', 'Ma2', 'Ba1',
                 'Ma3', 'Va1', 'Va2', 'Ma4', 'MaA', 'Ma5', 'MaB',
                 'Ma.5', 'MaB', 'Ma:C']

for elemento in listaCiudades:
    # Negamos el rango con ^ inicio
    if re.findall('Ma[0-3]', elemento):
        print(elemento)

print('- Varios rangos')
for elemento in listaCiudades:
    # Negamos el rango con ^ inicio
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)

print('- Filtramos por puntos')
for elemento in listaCiudades:
    # Negamos el rango con ^ inicio
    if re.findall('Ma[.:]', elemento):
        print(elemento)

print(' -- MATCH Y SEARCH')

nombreUno = 'Sandra López'
nombreDos = 'Antonio Gómez'
nombreTres = 'María López'
nombreCuatro = 'sadra López'
nombreCinco = 'Jara López'
nombreSeis = 'Lara López'

# Busca un patron de busqueda. (Distingue netre mayusculas y minisculas)
# Distingue netra mayúsculas y Minúsculas
if re.match('Sandra', nombreUno, re.IGNORECASE):
    print('Hemos encontrado el nombre')
else:
    print('No lo hemos encontrado')

print('- Ignoramos los espacios: ')
# Filtramos ignorado los espacios en el patron de busqueda
if re.match('S andra', nombreUno, re.VERBOSE):
    print('Hemos encontrado el nombre')
else:
    print('No lo hemos encontrado')

print('- Por caulquier inicio de letra: ')
# Filtramos ignorado los espacios en el patron de busqueda
if re.match('.ara', nombreSeis, re.IGNORECASE):
    print('Hemos encontrado el nombre')
else:
    print('No lo hemos encontrado')


print('- Cadena de textos que empiezen por uno: ')
cadenaUno = 'Jara López'
cadenaDos = '265165465413'
cadenaTres = 'a6151651654'

# Filtramos por números
if re.match('\d', cadenaUno):
    print('Hemos encontrado el número')
else:
    print('No lo hemos encontrado')

# Filtramos por números
if re.match('\d', cadenaDos):
    print('Hemos encontrado el número')
else:
    print('No lo hemos encontrado')


print('- Cadena de textos Toda la cdena de texto: ')
cadenaUno = 'Jara López'
cadenaDos = '265165465413'
cadenaTres = 'a6151651654'

# Filtramos letras
if re.search('López', nombreUno, re.IGNORECASE):
    print('Hemos encontrado el NOMBRE')
else:
    print('No lo hemos encontrado')

print('- Filtramos en cadenas largas')
codigoUno = 'acdadxsa71vddlifjvslnaldscx'
codigoDos = '71cddacakjasnca'
codigoTres = 'clsdhcnksahnck'

if re.search('71', codigoUno, re.IGNORECASE):
    print('Hemos encontrado el 71')
else:
    print('No lo hemos encontrado')