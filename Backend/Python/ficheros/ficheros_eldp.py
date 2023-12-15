'''

'''
print('--Abrimos un fichero con la funcion open (Modo lectura)--')
#Lee todas la lineas del fichero
lecturaUnoFichero = open('Backend/Python/ficheros/ejemplo.txt', encoding='utf-8')
print(lecturaUnoFichero.read())

print('--Método readline()--')
#Abre el fichero linea por linea
lecturaDosFichero = open('Backend/Python/ficheros/ejemplo.txt', encoding='utf-8')
print(lecturaDosFichero.readline())
print(lecturaDosFichero.readline())

print('--Leer todo el fichero por caracter--')
lecturaTresFichero = open('Backend/Python/ficheros/ejemplo.txt', encoding='utf-8')
caracter = lecturaTresFichero.readline(1)
while caracter !="":
    #print(caracter) #Esto lee el fichero por cada caracter
    caracter = lecturaTresFichero.readline(1)

print('--Uso del readlines() par devolverlo en una lsita--')
lecturaCuatroFichero = open('Backend/Python/ficheros/ejemplo.txt', encoding='utf-8')
lineas = lecturaCuatroFichero.readlines()
print(lineas)
#Iteramos esa lista
for i in lineas:
    print(i)
   
print('--Buenas practica para leer un fichero--')
leerFichero = open('Backend/Python/ficheros/ejemplo.txt', 'r', encoding='utf-8')

print('--Ficherons con excepciones--')
with open('Backend/Python/ficheros/ejemplo.txt', encoding='utf-8') as ficherpWith:
    #Aca el fichero se cerrara automaticamente
    pass

print('--Uso del readline() con with--')
with open('Backend/Python/ficheros/ejemplo.txt', encoding='utf-8') as ficheroDosWith:
    linea = ficheroDosWith.readline()
    while linea != '':
        print(linea, end='')
        linea = ficheroDosWith.readline()

print('\n--Uso del reallines()--')
with open('Backend/Python/ficheros/ejemplo.txt', 'r', encoding='utf-8') as ficheroLines:
    for linea in ficheroLines.readlines():
        print(linea, end= '')