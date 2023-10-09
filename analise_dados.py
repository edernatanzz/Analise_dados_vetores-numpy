import csv
import numpy as np

# Leitura dos dados do arquivo CSV e armazenamento em vetores
nomes = [] #vetores vazios para receber dados
total_vendas = []  #vetores vazios para receber dados
comissoes = [] #vetores vazios para receber dados

with open('dados_vendas.csv', mode='r') as arquivo_csv: #abre o arquivo csv vindo do exel
    leitor = csv.DictReader(arquivo_csv) # cria um leitor csv para leitura das linhas e colunas
    for linha in leitor: #pecorre as linhas e colunas armazenando os dados 
        nomes.append(linha['Nome']) # dados da primeira linha
        total_vendas.append(float(linha['Total_Vendas']))# dados da 2 coluna referente a total de vendas
        comissoes.append(float(linha['Comissao'])) # dados 3 coluna referente a comissão dos funcionarios

# Conversão das listas em vetores numpy
total_vendas = np.array(total_vendas) #convertidos de listas Python para vetores NumPy 
comissoes = np.array(comissoes) #convertidos de listas Python para vetores NumPy 

# Encontrar os 2 funcionários que mais venderam usando argsort ---> retorna os índices que classificam o vetor em ordem crescente, e [::-1] inverte a ordem para que os maiores valores apareçam primeiro. [:2] pega os dois primeiros índices.
indices_mais_venderam = np.argsort(total_vendas)[::-1][:2]#[::-1] inverte a ordem para que os maiores valores apareçam primeiro. [:2] pega os dois primeiros índices.
funcionarios_mais_venderam = [(nomes[i], total_vendas[i]) for i in indices_mais_venderam]

# Encontrar os 2 funcionários com menor comissão usando argsort
indices_menor_comissao = np.argsort(comissoes)[:2]#calcula os índices dos funcionários com menor comissão da mesma maneira que foi feito para os que mais venderam.
funcionarios_menor_comissao = [(nomes[i], comissoes[i]) for i in indices_menor_comissao] #é uma lista de tuplas contendo o nome e a comissão dos dois funcionários com menor comissão.

# Exibir os resultados
print("Os 2 funcionários que mais venderam:")
for nome, total_vendas in funcionarios_mais_venderam:
    print(f"{nome} - Total de Vendas: {total_vendas}")

print("\nOs 2 funcionários com menor comissão:")
for nome, comissao in funcionarios_menor_comissao:
    print(f"{nome} - Comissão: {comissao}")
    
print()
