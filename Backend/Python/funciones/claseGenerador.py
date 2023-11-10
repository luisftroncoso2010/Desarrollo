class AlCuadrado:
    def __init__(self):
        self.i = 0
        
    def __iter__(self):#Este metodo trabaja en conjunto con el metodo next
        return self#Desde aca se define como se comporta un obejto en un bucle
    
    def __next__(self):#Este se utuliza para obtener dicho valor de ese bucle
        if self.i>9:
            raise StopIteration
        
        result = self.i ** 2
        self.i +=1
        return result
eleva_al_cuadrado = AlCuadrado()
for i in eleva_al_cuadrado:
    print(i)
    
print('--Primeros 100 numeros naturales--')
def primerosN(n):
    nums = 0
    for i in range(n):
        yield nums
        nums += 1
    return nums
print(sum(primerosN(100)))

print('--Primeros 100 numeros aññadidos a una lista--')
def primerosCien(n):
    nums = list()
    for i in range(n):
        nums.append(i)        
    return nums    
print(sum(primerosCien(100)))

    
