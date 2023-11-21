'''
Leer archivos txt de manera correctiva y optima.
A esto se le donomina GESTORES DE CONTEXTO
'''
with open("D:/Desarrollo/Backend/Python/archivotxt/txt.txt", encoding= 'UTF-8') as archivo:
    print('Ejecutando el archivo....↓↓↓')
    print(archivo.read())
    #No es necesario cerrar el archivo
