'''
Trabajaremos con archivos csv.
Para trabajar cono csv se recomienda trabajar con el modulo csv
o en el mejor de los casos con el modulo pandas (as 'pd')
'''
#Importamos archivos csv
import csv
with open("D:/Desarrollo/Backend/Python/archivocsv/csv.csv", encoding= 'UTF-8') as archivo:
    reader = csv.reader(archivo)#Esto es un iterable    
    for row in reader:#Recorremos fila por fila. 
        print(row)#Cada fila se almacena por lista
    
   
    
    