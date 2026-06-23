vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604)]

# crie uma lista com as vendas de 2019
lista_vendas2019 = []
for produto,vendas2019,vendas2020 in vendas_produtos:
    lista_vendas2019.append(vendas2019)

lista_vendas2019.sort(reverse=True)
print(lista_vendas2019)

# Resolução de cima com list comprhensible 

lista_vendas2019_2 = [vendas2019 for produto, vendas2019, vendas2020 in vendas_produtos]

lista_vendas2019_2.sort(reverse=True)
print(lista_vendas2019_2)

# QUAL O MAIOR VALOR DA LISTA DE 2019?
print(max(lista_vendas2019))
print(max(lista_vendas2019_2))

# QUAL O PRODUTO QUE MAIS VENDEU NA LISTA DE 2019 
lista_vendasproduto2019 = [(vendas2019, produto) for produto, vendas2019, vendas2020 in vendas_produtos]
print(max(lista_vendasproduto2019))


