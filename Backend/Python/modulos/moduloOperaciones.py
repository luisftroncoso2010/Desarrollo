'''
Creamos operaciones en este modulo, para poderlas
importar. 
'''
def suma(a, b):
    return(a + b)

def resta(a, b):
    return(a - b)

def multiplicacion(a, b):
    return (a * b)
#Si olocamos el main de esta manera. El mensaje solo se ejecutara dentro del modulo, no fuera de este. 
#if __name__ == '__main__':#aca si seejecuta el mensaje por que le modulo esta en su propio main
#    print('Este es el modulo operaciones')

if(__name__ == '__main__'):    
    print(suma(4,4))