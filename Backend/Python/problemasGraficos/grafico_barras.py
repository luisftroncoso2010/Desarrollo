'''
Ingresos cofla
'''
import pandas as pd #Trabajo de csv 
import matplotlib.pyplot as plt #Visualizacion de datos
import seaborn as sns #Graficos estadadisticos
df = pd.read_csv("Backend//Python//problemasGraficos//cofla_ingresos.csv")
print(df)

#Creamos el grafico. barplot(Grafico de barras)
sns.barplot(x='fuente', y='ingresos', data=df)



#Calculando total ingresos
totalIngresos = df['ingresos'].sum()
#Mostrando el total de ingresos
print(f'Mostrando total ingresos de cofla: {totalIngresos} USD')

#Mostramos el grafico
plt.show()