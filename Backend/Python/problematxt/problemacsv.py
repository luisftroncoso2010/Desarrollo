'''
Cambiar el tipo de dato de una columna
'''
import pandas as pd 
df = pd.read_csv("Backend//Python//problematxt//csv.csv")
print(df)
print('Cambiamos la columna edad')
#Convertimos a String los datos de una columna
df['edad'] = df['edad'].astype(str)
#Mostrar los datos del primer elemento de la columna edad
print(type(df['edad'][0]))
#Remplazar datos/valores (existente, nuevo, implace)
df['nombre'].replace('alejo', 'cr7', inplace=True)
print(df['nombre'])
#Eliminar filas con datos faltantes
df = df.dropna()
print(df)
#Eliminando las filas repetidas
df = df.drop_duplicates()
print(df)
#Guarda data frame LIMPIO
df.to_csv("Backend//Python//problematxt//csvlimpio.csv")
