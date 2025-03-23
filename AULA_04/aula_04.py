#Importar pacotes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Carregar dataframe
caminho = 'AULA_04/Vídeo+4.1.xlsx'

df = pd.read_excel(caminho)

#Plotar gráfico
plt.plot(df['Data'], df['Número de livros vendidos'])
plt.show()

#Medidas
print(f'Média dos números de livros vendidos: {np.median(df["Número de livros vendidos"])}')
print(f'Desvio Padrão dos números de livros vendidos: {np.std(df["Número de livros vendidos"])}')
