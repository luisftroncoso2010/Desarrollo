print('-----Ejemplo edad------')
edad = 17
if edad >= 18 & edad <= 25:
    print('Es mayor de edad pasado a adulto')
elif edad > 25:
    print("Estas en edad adulta")
else:
    print ('No es mayor aun')
    
print('---Otro Ejemplo------')
fav = "mundogeek.net"
if fav == "mundogeek.net":
    print ("Tienes buen gusto")
    print('Gracias!')
    
print('---else-----')
fav = "mundogeek.net"
if fav == "mundogeek.net":
    print ("Tienes buen gusto")
    print('Gracias!')
else:
    print('Vaya, que lastima')
    
print('---else if---')
numero = 1
if numero < 0:
    print(numero,"es negativo.")
elif numero > 0:
    print('Positivo')
else:
    print('Cero')
    
print('---A if C else B---')
num = 2
var = "Par" if (num % 2 == 0) else "Impar"
print(var)