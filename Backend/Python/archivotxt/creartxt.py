'''
Crearemos un archivo txt
'''
with open("D:/Desarrollo/Backend/Python/archivotxt/archivotxt.txt", mode='a', encoding='UTF-8') as archivo:
    '''
    Crearemos un arhchivo con unos textos
    '''
    file_archivo = archivo.read()
    print(file_archivo)