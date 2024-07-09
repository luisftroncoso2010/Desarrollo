print(' * Generadores: ')

lista = [1, 5, 7]
generador = (n ** 2 for n in lista)


def mi_generador(n, m, s):
    while (n <= m):
        yield n
        n += s


generador = mi_generador(0, 5, 2)
print(next(generador))
print(next(generador))


print(' * Mostrar todo el contenido del generador:')
"""
Nota: Aca se puede itera el generador para
que muestre todo el contenido del generador
"""
for i in mi_generador(0, 5, 2):
    print(i)
