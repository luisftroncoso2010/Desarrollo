'''
Numeros primos desde el 0 hasta el que se le pasa
'''
def esPrimo(num):
    for i in range(2, num-1):
        if num % i ==0: 
            return False
    return True 

def primosHasta(num):
    primos = []
    for i in range(2, num+1):
        resultado = esPrimo(i)
        if resultado == True: 
            primos.append(i)
    return primos
    
resultado = primosHasta(13)
print(resultado)
