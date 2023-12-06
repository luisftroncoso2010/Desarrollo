''' Exepciones: '''
#La funcion suma
def suma_dos():  
    #Metemos esto en while para que se ejecute mientras se pueda  
    while True:
        #Pedimos los datos por ocnsola        
        a = input('Nuemro 1: ')
        b = input('Numero 2: ')
        try:#Generamos la excepsion. Se genera la excepcion cuando se pida de tal manera por el usuario
        #Vamos a colocar el el numero a de manera String cuando se pida por el usuario
            resultado = int(a) + int(b)                       
        except ValueError as e: #Accedemos a todas la eception
            print('Por favor no te detengas. coloca un numero de tipo int')
            print(f'Error: {e}')#Me mostrara a la exepsion y el valor de donde salio la axcepsion, mas el nombre
        else:#Este se ejecutara solo SI NO HAY ERROR           
            break #Cierra de tal manera cuando NO hay error
        finally: #Se ejecuta si o si, haya error o no.
            print('Esto simepre se ejecutrará')
    return f'Operacion realizada. {resultado}'
suma_dos()

print('--Exepcion divicion en cero--')
def divicionCero(a, b):
    #Creamos el ciclo while para que se ejecute siempre y cuando pida (True)
    while True:
        a =input('Dame el valor de a: ')
        b = input('Dame el numero de B: ')
        try:
            resultado = int(a) / int(b)
        except ZeroDivisionError:#Se coloca cuando se va a dividir entre cero
            print('No se puede hacer una division entre 0, ni ocn datos de tipo String')
        else:
            print('Operacion resuelta')
            
#Instanciamos la funcion
divicionCero(10, 0)
    

    