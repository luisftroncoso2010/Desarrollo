'''
Escribir un archivo tx.

'''
with open("D:/Desarrollo/Backend/Python/archivotxt/archivotxt.txt", 'r', encoding= 'UTF-8') as archivo:
    '''Sobre escribiendo el archivo con la funcion write()'''
    #Agregamos archivos append. Usamos un bucle para agregar varias lineas
    fileRead = archivo.readline()#Limitara el numero de caracteres
    print(fileRead)
  
    
    