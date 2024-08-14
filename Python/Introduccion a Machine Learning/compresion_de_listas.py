""" compresion de lisas. (En que motivos se usará)"""

# Generar una lista apartir de otra
curso = []
for letras in 'python':
    curso.append(letras)
print(curso)

# Creamos una lista por compresión
cursoDos = [letras for letras in 'python']
print(cursoDos)

# Lista apartir de otra
listaA = [1, 2, 3, 4, 5]
listaB = []

for i in listaA:
    paraListaB = i * 2
    listaB.append(paraListaB)
    print(listaB)

# Generar una lista por otra lista por compresion
listaBDos = [i * 4 for i in listaA]
print(listaBDos)
