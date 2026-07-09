import numpy as np

vendas = np.array([
    [120, 150, 180, 200],
    [90, 110, 130, 125],
    [210, 220, 215, 230],
    [140, 160, 170, 165]
])

'''
O gerente pediu:
Quanto cada vendedor vendeu no total? sim
Qual vendedor teve a maior venda individual? sim 
Em qual trimestre cada vendedor vendeu mais? sim
Qual foi a maior venda registrada? sim
Qual foi a menor venda registrada?
Quantas vendas foram maiores ou iguais a 200?
Mostre somente as vendas maiores ou iguais a 200.
'''

total_vendas_cada_vendedor = vendas.sum(axis=1)
maiores_vendas = vendas.max(axis=1)
maior_venda_individual = np.argmax(maiores_vendas)
trimestre_que_cada_vendedor_vendeu_mais = vendas.argmax(axis=0)
maior_venda_registrada = vendas.max()
menor_venda_registrada = vendas.min()
vendas_maiores_ou_iguais_a_200 = np.sum(vendas >= 200)
somente_maiores_ou_iguais_a_200 = vendas[vendas >= 200]

print(f'Total de vendas de cada vendedor: {total_vendas_cada_vendedor}')
print(f'Maior venda individual: {maior_venda_individual}')
print(f'Trimestre em que cada vendedor teve mais vendas: {trimestre_que_cada_vendedor_vendeu_mais}')
print(f'Maior venda registrada: {maior_venda_individual}')
print(f'Menor venda registrada: {menor_venda_registrada}')
print(f'Quantidade de vendas maiores ou iguais a 200:  {vendas_maiores_ou_iguais_a_200}')
print(f'Vendas maiores ou iguais a 200 que foram realizadas: {somente_maiores_ou_iguais_a_200}')



