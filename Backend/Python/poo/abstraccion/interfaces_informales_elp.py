from abc import ABC, abstractclassmethod, ABCMeta
''' Interfaces informales: Puede ser definida con una simple clase
que no implementa los metodos'''
#Creamos la clase
#Ya que en python como tal el concepto NO EXISTE. 
# Creamo una clase que no implementa los metodos
print('---interfaces informales---')
class Mando:
    #Metodos
    def siguiente_canal(self):
        pass        
    def canal_anterior(self):
        pass        
    def subir_volumen(self):
        pass        
    def bajar_volumen(self):
        pass

#Cremamos la siguiente clase, atraves de la herencia para implementar los metodos
class MandoSamsung(Mando):
    #Metodos
    def siguiente_canal(self):
        print('Samsung -> Siguiente')        
    def canal_anterior(self):
        print('Samsung -> Anterior')       
    def subir_volumen(self):
        print('Samsung -> Subir')        
    def bajar_volumen(self):
        print('Samsung -> Bajar') 

#Creamos la siguiente clase, atraves de la herencia para implementar los metodos
class MandoLG(Mando):
    #Metodos
    def siguiente_canal(self):
        print('LG -> Siguiente')        
    def canal_anterior(self):
        print('LG -> Anterior')       
    def subir_volumen(self):
        print('LG -> Subir')        
    def bajar_volumen(self):
        print('LG -> Bajar')

''' NOTA: Al hacer una interfas informal ATRAVES de herencia NO 
se obliga a las sub clases a implmentar los metodos, lo cual esto 
a la larga puede causar problemas '''
