def lisar_produtos(*listas):
    lista_produtos = []
    for lista in listas:
        for produto,estoque in lista:
            lista_produtos.append(produto)
