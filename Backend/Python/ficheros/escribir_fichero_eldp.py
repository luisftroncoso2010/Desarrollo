''' Escribir un fichero '''
with open('Backend/Python/ficheros/fichero.txt', 'r', encoding='utf-8') as fichero:
    for linea in fichero.readline():
        print(linea, end='')
        
print('--Crear una un fiechero a partir de una lista--')
#Abrimos el fichero
ficheroLsita = open('Backend/Python/ficheros/ficheroLista.txt', 'w', encoding='utf-8')
#Tenemos unos datos que queremos guardar
lista = ['Manzana', 'Pera', 'Plátano']#Creamos la lista
#Guardamos la lista en el fichero
for linea in lista:
    ficheroLsita.write(linea + '\n')
#Cerramos el fichero
ficheroLsita.close()#Aca se cierra el fichero ya creado

print('--Creamos un fichero partir de una lista. Metodo write()--')
#abrimos el fichero. S in oexiste se crea
f = open('Backend/Python/ficheros/ficheroo.txt', 'w', encoding='utf-8')
#Tenemos uno datos ne lal ista que guardaremos
listaFichero = ['Manzana', 'Pera', 'Plátano']
#Huradamos la lisa en el fichero
for linea in listaFichero:
    f.write(linea + '\n')#Se agrega los datos linea por linea
#Cerramos el fichero
f.close()    

print('--Metodo writelines()--')#Creamoa el fichero
ficheroWritelines = open('Backend/Python/ficheros/fiicheroo.txt', 'w', encoding='utf-8')
for linea in listaFichero:
    ficheroWritelines.write(linea + '\n')   
ficheroWritelines.close() 

print('--Leer un fichero, ciclo for()--')
with open('Backend/Python/ficheros/fiicheroo.txt', 'r', encoding='utf-8') as ficheroread:
    for linea in ficheroread.readlines():
        print(linea, end='')

print('--Leer un fichero con with open y readline()--')
#Con el with el fichero de abre y se cierra 
with open('Backend/Python/ficheros/fiicheroo.txt', 'r', encoding='utf-8') as fiche:
    for linea in fiche.readlines():#Recorremos linea por linea
        print(linea, end ='')#Recorremos linea por linea

print('--Crear y abrir un fichera, writelines()--')
#Creamos el fichero
ficheroLista = open('Backend/Python/ficheros/datos_guardados.txt', 'w')
#Lista de frutas para añadir al archivo
listaFrutas = ['Manzana\t', 'Pera\t', 'Platano\t']
ficheroLista.writelines(listaFrutas)
ficheroLista.close()
with open('Backend/Python/ficheros/datos_guardados.txt', 'r', encoding='utf-8') as fich:
    for linea in fich.readlines():
        print(linea, end='')


        


        


