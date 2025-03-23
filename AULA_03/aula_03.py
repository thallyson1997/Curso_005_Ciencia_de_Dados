#Importar pacotes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Carregar dataframe
caminho = 'AULA_03/Vídeo+3.1.csv'

df = pd.read_csv(caminho).iloc[5:]

#Renomear o dataframe
colnames = ["Titulo", "Isbn", "Autor", "Assunto", "Valor"]

for i in range(0, len(colnames)):
    df = df.rename(columns={list(df.columns)[i]:colnames[i]})

#Carregar outro dataframe
caminho = 'AULA_03/Vídeo+3.2.xlsx'

df = pd.read_excel(caminho)

#Realizar interpolação
df_interpolado = df.copy()

lista = []

for i in range(0, len(df['Acessos'])):
    if str(df["Acessos"][i]) == 'nan':
        lista.append((df["Acessos"][i - 1] + df["Acessos"][i + 1]) / 2)
    else:
        lista.append(df["Acessos"][i])

df_interpolado['Acessos'] = lista

#Plotar gráfico
fig, axs = plt.subplots(2)
axs[0].plot(df["Data"], df["Acessos"])
axs[1].plot(df_interpolado["Data"], df_interpolado["Acessos"])
plt.show()