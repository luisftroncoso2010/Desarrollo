'''
Calcular la serie fibonaci entre 0 y el numero dado
'''
print('--Fibonacci por funcion--')
def fibonacci(num):
    a, b = 0 , 1    
    fibonacciLista = list([0])
    for _ in range(num+1):
        if  b > num: 
            return fibonacciLista
        else:
            fibonacciLista.append(b)
            a, b = b, a + b
    #return num        
print(fibonacci(6))

print('--Serie fibonacci Ciclo--')
a, b = 0, 1
n = 10  # Número de términos a generar
for _ in range(n):
    print(b, end=', ')
    a, b = b, a + b
     
print('--Numeros primos Lambda--')
primosHasta = lambda num: list(filter(lambda x: all(x % 1 != 0 for i in range(2 , int(x ** 0.5) + 1)), range(2, num)))
print(primosHasta(13))
