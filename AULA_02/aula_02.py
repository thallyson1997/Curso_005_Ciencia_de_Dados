#Bibliotecas importadas
import pandas as pd
import matplotlib.pyplot as plt

#Ler o arquivo .xlsx
caminho = 'AULA_02/Vídeo+2.1.xlsx'

df = pd.read_excel(caminho)

#Como tem muitos NaN e varias tabelas, vamos fragmentar.
df1 = df.iloc[0:5,0:2]
df2 = df.iloc[60:75,0:2]

#Criar gráfico
plt.bar(df1['Estilo'], df1['Vendas'])
plt.show()
plt.bar(df2['Estilo'], df2['Vendas'])
plt.show()