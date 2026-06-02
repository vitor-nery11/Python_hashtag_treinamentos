#exercicio de data science 


precos_imoveis = [
    2.17, 1.54, 1.45, 1.94, 2.37, 2.30, 1.79, 1.80, 2.25,
    1.37, 2.40, 1.72, 2.00, 1.69, 1.63, 2.01, 2.25, 1.61,
    1.02, 1.19, 1.86, 2.15, 2.00, 1.58, 1.73, 2.12, 1.95
]

tamanho_imoveis = [
    207, 148, 130, 203, 257, 228, 160, 194, 232,
    147, 222, 165, 184, 175, 147, 217, 214, 171,
    86, 111, 180, 211, 210, 168, 156, 154, 179
]

def separar_listas(precos,tamanhos, fator = 0.1):
    if len(precos) == len(tamanhos):
        i = int((1 - fator) * len(precos))
        preco_imoveis_treino = precos_imoveis[:i]
        preco_imoveis_teste = precos_imoveis[i:]
        tamanho_imoveis_teste = tamanho_imoveis[i:]
        tamanho_imoveis_treino = tamanho_imoveis[:i]
        return tamanho_imoveis_treino, tamanho_imoveis_teste, preco_imoveis_treino, preco_imoveis_teste
    else:
        print('A lista de preços e tamanhos não tem a mesma quantidade de itens')
        return
    

print(len(precos_imoveis))
precos_treino, preco_teste, tamanho_treino,tamanho_teste = separar_listas(precos_imoveis, tamanho_imoveis)
print(preco_teste)