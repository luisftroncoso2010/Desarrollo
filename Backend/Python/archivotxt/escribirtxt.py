'''
Escribir un archivo tx
'''
with open("D:/Desarrollo/Backend/Python/archivotxt/txt.txt", 'w', encoding= 'UTF-8') as archivo:
    '''Sobre escribiendo el archivo con la funcion write()'''
    #archivo.write('He sobre reescrito el archivo')
    
    '''Aca se le puede pasar un iterable'''
    archivo.writelines(['Hola luis como andas\n', 'Luis\n', 'Troncoso\n'])#Se almacena por debajo de la linea
    '''Aca se le puede pasar otro iterable un iterable'''
    archivo.writelines(['luis\n', 'Luis ', 'Montes'])  
    
    '''NOTA: La funcion anterior resive el iterable y lo pasa
    de tal manera que quede igual'''
