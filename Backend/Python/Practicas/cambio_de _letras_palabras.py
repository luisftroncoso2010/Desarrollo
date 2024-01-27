'''Cambio de letras por palabras.
Se desea cambiar el nombre que tiene una lista de nombres'''

print('-- Cambio de letras por números en nombre.')


# Creamos el set e nombres
nombres = ["JUAN", "EVELIN", "ANA", "MARK", "DIEGO", "ABCD", "ZY"]
# Creamos el sets de abecedario
abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
# Creamos el set de numeros de remplazo (Numero iguales que el abecedario)
númerosABC = list(range(1, 28))


# Iniciamos la variable para con tar el ciclo
x = 0
# Creamoa la variable auxiliar. Amacenaremos los que ya van
nombreAuxiliar = ''

# Contamos los elementos del set nombre, para iniciar el ciclo
NUMERODEELEMENTOS = len(nombres)


# Iniciamos el ciclo con el valor del set nombres
while x < NUMERODEELEMENTOS:
    # Iteramos sobre los caracteres de los elementos del set nombres
    for letra in nombres[x]:
        # Iteramos sobre el set Abecedario
        for indice, letra_abecedario in enumerate(abecedario):
            # Condicion para comparar cada caracter de los elementos
            # Del set abecedario
            if letra == letra_abecedario:
                nombreAuxiliar += str(númerosABC[indice])
    print(f'Nombre: {nombres[x]}\tNumero: {nombreAuxiliar}')
    nombreAuxiliar = ''
    x += 1
