import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Backend//Python//problemasGraficos//bigotes.csv")
print(df)

#Creando grafico y de bigotes
'''
Mostrara la distribucion de datos en cuartiles, 
resaltando el promedio y los valores atipicos
'''
sns.boxplot(x='categoria', y='valores', data=df)

#Mostando grafico
plt.show()