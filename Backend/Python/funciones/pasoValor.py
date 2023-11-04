'''
Paso por valor y referencia
'''
print('--Valor y referencia--')
x = 10
def funcion(entrada):
    entrada = 0
    print(entrada) #El valor que adquiere la funcion es la pasada por parametro
funcion(x)
print(x) # 10

print('--Paso por valor lista')
listNum = [10, 20, 30]
def funcion(entrada):
    print(listNum)#Aca si se modifica dado que es un objeto mutable
    entrada.append(40) 
funcion(listNum)
print(listNum) # [10, 20, 30, 40]