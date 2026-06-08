produtos = {
    "Notebook": 3500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 1200
}

def produto_mais_caro(produtos):
    maior_valor = 0
    for produto, valor in produtos.items():
        if valor > maior_valor:
            maior_valor = valor
        return maior_valor
    

    
print(produto_mais_caro(produtos))