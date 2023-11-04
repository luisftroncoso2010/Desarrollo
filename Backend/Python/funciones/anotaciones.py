'''
Anotaciones en funciones
'''
print('--Anotaciones de funciones--')
def suma(a: int, b: int) -> int:
    return a + b
print(suma(7,3))

print('--ANotaciones de tipo VAR--')
def imprime(var):#Resitve cualquier tipo de varible
    print(var)
imprime(1.0)
imprime(3)
imprime('Python')

print('--Ejemplos de annotations--')
def filtrarPares(salida: list = []) -> list:
    return [i for i in salida if i%2==0]
print(filtrarPares([1,2,3,4,5,6,7,8]))

print('--Suma Dos--')
def sumaDos(a: int, b: int) -> int:
    return a + b
print(sumaDos(4, "6.2"))