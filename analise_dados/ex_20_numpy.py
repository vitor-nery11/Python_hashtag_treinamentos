import numpy as np

vendas = np.array([
    [12, 15, 18, 20],
    [10, 14, 13, 16],
    [20, 22, 19, 25],
    [8, 12, 15, 14]
])

'''
O gerente pediu:
Quanto cada vendedor vendeu no total?
Quanto foi vendido em cada semana?
Qual vendedor teve a maior média de vendas?
Qual semana teve a maior média de vendas?
Qual foi a maior venda registrada?
Qual foi a menor venda registrada?
Quantos registros possuem vendas maiores ou iguais a 20?
Mostre apenas as vendas maiores ou iguais a 20.
'''

# logica
total_vendas_cada_vendedor = vendas.sum(axis=1)
total_vendas_cada_semana = vendas.sum(axis=0)
media_vendas_cada_vendedor = vendas.mean(axis=1)
maior_media_vendas_vendedores = np.max(media_vendas_cada_vendedor)
media_vendas_cada_semana = vendas.mean(axis=0)
maior_media_vendas_semana = np.max(media_vendas_cada_semana)
maior_venda = vendas.max()
menor_venda = vendas.min()
quantidade_vendas_maiores_ou_iguais_a_20 = np.sum(vendas >= 20)
vendas_maiores_ou_iguais_a_20 = vendas[vendas >= 20]



# relatorio
print(f'Total de vendas realizadas por cada vendedor: {total_vendas_cada_vendedor}')
print(f'Total de vendas realizadas por cada semana: {total_vendas_cada_semana}')
print(f'Maior media de vendas por vendedor: {maior_media_vendas_vendedores}')
print(f'Maior media de vendas por semana: {maior_media_vendas_semana}')
print(f'Maior venda feita: {maior_venda}')
print(f'Menor venda: {menor_venda}')
print(f'Quantidade de vendas maiores ou iguais a 20: {quantidade_vendas_maiores_ou_iguais_a_20}')
print(f'Vendas maiores ou iguais a 20: {vendas_maiores_ou_iguais_a_20}')





