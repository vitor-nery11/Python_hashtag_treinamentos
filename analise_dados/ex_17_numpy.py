import numpy as np

'''
Requisitos

Escreva um programa que mostre:

Todos os notebooks que custam R$ 3.000 ou mais.
Todos os notebooks que custam menos de R$ 2.500.
Quantos notebooks custam mais de R$ 4.000.
Quantos notebooks custam menos de R$ 3.000.
O notebook mais caro.
O notebook mais barato.
O preço médio dos notebooks.
'''

precos = np.array([2500, 3200, 1800, 4500, 2900, 5100, 1999, 3800, 4200, 2700])

notebooks_3000_acima = precos[precos>=3000]
notebooks_2500_menos = precos[precos<2500]
notebooks_4000_acima = np.sum(precos>4000)
notebooks_3000_menos = np.sum(precos<3000)
notebook_mais_caro = np.max(precos)
notebook_mais_barato = np.min(precos)
preco_medio = np.mean(precos)

print(f'Preços de notebooks acima de 3000: {notebooks_3000_acima}')
print(f'Precos de notebooks abaixo de 2500: {notebooks_2500_menos}')
print(f'Quantidade de notebooks acima de 4000: {notebooks_4000_acima}')
print(f'Quantidade de notebooks abaixo de 3000: {notebooks_3000_menos}')
print(f'Preço do notebook mais caro da loja: {notebook_mais_caro}')
print(f'Preço do notebook mais barato da loja: {notebook_mais_barato}')
print(f'Preço médio dos notebooks: R$ {preco_medio:.2f}')




