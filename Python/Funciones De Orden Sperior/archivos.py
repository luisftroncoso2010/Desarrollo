""" Leer el archivo"""
print(" * ")
archivo = open("archivo.txt", "r")  # Aca está en modo escritura
contenido = archivo.read()
print(contenido)
archivo.close()


print("  * Leyendo el archivo de linea por linea por linea: ")


archivoDos = open("archivo.txt", "w")
archivoDos.write("Hola andres.\n")
archivoDos.write("Andres, ¿Como estas?.\n")

for lines in archivoDos.readlines():
    print(lines)

archivoDos.close()


"""
Nota: reaLine() solo funciona cuanod en una linea solo hay una declaracion
readLines() funciona con muchas lineas. Es decir, muestra varia declaraciones
"""

# while True:
#     linea = archivoDos.readline()
#     if not linea: break
#     print(linea)


"""
Nota: En algunas instancias es mejor tomar por consideracion
es mejor usar el bloque with open
"""
