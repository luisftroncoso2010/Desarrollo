#Funcon contar letras 
def contar_letrar(frase):
    numero_letras = 0
    for i in frase:
        if i != ' ':
            numero_letras +=1
    return numero_letras
            

        