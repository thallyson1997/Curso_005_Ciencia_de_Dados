#Bibliotecas importadas
import pandas as pd

#Ler o arquivo .txt
caminho = 'AULA_01/aula1_1/aula1_1.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

#Crie o dataframe
linhas = [linha.strip() for linha in linhas]
linhas = [linha for linha in linhas if linha not in ['']]

indice_divisor = linhas.index('========================================')

livros = linhas[1:indice_divisor]
quanti = linhas[indice_divisor+2:]

df = pd.DataFrame({
    'Livro': livros,
    'Quantidade': [int(q) for q in quanti]
})

#Adicione o preço
caminho = 'AULA_01/aula1_2/aula1_2.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

preco = [float(linha.strip().replace(',','.')) for linha in linhas]
df['Preço'] = preco

#Adicione a venda
df['Venda'] = df['Preço'] * 1.4

#Somando os valores
total_quantidade = sum(df['Quantidade'])
total_preco = sum(df['Preço'])
total_venda = sum(df['Venda'])
print(total_quantidade)
print(f'R$ {total_preco:.2f}')
print(f'R$ {total_venda:.2f}')