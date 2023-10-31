print('---For---')
print('---Ejemplo iterar en una lista---')
secuencia = ['uno', 'dos', 'tres']
for elemento in secuencia: #
    print(elemento)
    
print('---Ejemplo ciclo FOR con range---')
for numero in range(2, 11, 2):
    print(numero)

print('---While---')
print('---Ejemplo edad---')
edad = 0  
while edad < 18:    
    edad = edad + 1
    print(f'Felicidades tienes {str(edad)} años')    
    
print('---Ejemplo imput WHILE, pedir datos por consola---')
while True:
    entrada = input('>') #Se pide el dato "Adios" por consola para comparar si es igual o no. 
    if entrada == 'Adios':
        break #Si cumple la condicion el buble se cierra con break(Español, romper)
    else:
        print(entrada)
        
print('--- Otro ejemplo while pero sin el break---')
salir = False 
while not salir: # Se niega la variable para que el programa lo pueda compilar, es decir se paasa a True ya que se iniciliza en False
    entrada2 = input('>')
    if entrada2 == 'Adios':
        salir = True # Aca no se niega la variable, para que le programa pueda salir. 
    else:
        print(entrada2)
        
edad2 = 0
while edad2 < 18:
    edad2 = edad2 + 1
    if edad2 % 2 == 0:
        continue # Aca quitamos las edades que son para, si tiene una edad par la quita y continua ocn la proxima iteracion.
    print(f'Felicitaciones tienes {str(edad2)} años')
    


    
    
    
    