import numpy as np

vendas = np.array([
    [120, 150, 180, 200],
    [90, 110, 130, 125],
    [210, 220, 215, 230],
    [140, 160, 170, 165]
])

'''
O gerente pediu:
Quanto cada vendedor vendeu no total?
Qual vendedor teve a maior venda individual?
Em qual trimestre cada vendedor vendeu mais?
Qual foi a maior venda registrada?
Qual foi a menor venda registrada?
Quantas vendas foram maiores ou iguais a 200?
Mostre somente as vendas maiores ou iguais a 200.
'''

total_vendas_cada_vendedor = vendas.sum(axis=1)
maiores_vendas = vendas.max(axis=1)
maior_venda_individual = np.argmax(maiores_vendas)
print(maior_venda_individual)

