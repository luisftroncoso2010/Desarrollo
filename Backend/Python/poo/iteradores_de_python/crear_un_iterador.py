'''
Crear un iterador: 
Para crear un obejto/clase como iterador, debe implementar los metodos
__iter__() y __next__() su objeto
'''
#Ejemplo
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a +=1
        return x
objeto = MyNumbers()
#el metodo iter() es que que va a iterar al objeto de la mano con next()
myIter = iter(objeto)
#Imprimimos myIter con el objeto
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
#Cuantas veces lo imprimamos, seguirá sumando numeros
print(next(myIter))
print(next(myIter))

print('Stop Iteration con for')
class Mynumbers:
    #Se crea el metodo iterable, que va desde uno
    def __iter__(self):
        self.a = 1
        return self
    #Metodo especial para iterar
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
        
#Se crea el objeto para iterar
objetoTwo = Mynumbers()#Se intanacia la clase
myiter = iter(objetoTwo)#Con el metodo iter() se itera

for x in myiter:
    print(x)

        