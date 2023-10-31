'''
Crear mis propias funciones
'''
#creando una funcion simple
print('--funcon simple--')
def saludar ():
    print('Hola lucas maestro, ¿como andas?')    
saludar()

#Crear una funcion que tenga parametros
print('--Saludar a lucas por parametro')
def saludarLucas(nombre):
    print(f'Hola {nombre}, mi maestro, ¿Como andas?')
saludarLucas('Luis')

print('--Saludar a maestro por nombre/sexo--')
def saludarDos(nombre, sexo):
    sexo = sexo.lower() #convierte todo a mayusculas
    if(sexo == 'mujer'):
        adjetivo = 'mi reina'
    elif(sexo == 'hombre'):
        adjetivo = 'titan'
    else:
        adjetivo= 'amor'     
    print(f'Hola {nombre}. mi {adjetivo}, ¿Como estas?')
saludarDos('Camila', 'mujer')
saludarDos('Luis', 'hombre')
saludarDos('no me defino', '')

#crar una funcion que nos retrne valorees
print('--Crear una funciom con return--')
def crearContraseña(num):    
    chars = 'fknvlsknlksvnfd'
    #numero_entero = str(num)    
    #num = int(numero_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return print(contraseña)

crearContraseña(3)