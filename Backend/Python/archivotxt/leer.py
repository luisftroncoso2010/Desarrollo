archivo = open("D:/Desarrollo/Backend/Python/archivotxt/txt.txt", encoding= 'UTF-8')
'''
Un archivo una ves ya leido no se puede volver a leer, para volverlo 
a leer hay que cerrarlo
'''
#Leer archivocompleto 
#archivo = archivo_sin_leer.read()

#Almacenar linea por linea en una lista
#lineaList = archivo.readlines()
#Te mostrara un \n por que la linea siguiente la separará por un una coma

'''Lee linea por linea y se le pasa un un numero como argumento,
es le numero de caracteres que leerá'''
lineaList = archivo.readline(1)
archivo.close()

print(archivo.read())#No se puede volver a leer por que ya se cerró
'''
Se debe volver a usar la funcion open para volver a abrir el archivo
'''