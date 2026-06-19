preco_produto = [100,150,300,5500]

imposto = [preco * 0.3 for preco in preco_produto]

print(imposto)

def calcular_imposto(preco, imposto):
    return preco * imposto 

imposto = [calcular_imposto(preco, 0.3) for preco in preco_produto]

