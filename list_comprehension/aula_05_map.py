produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']

def padronizar_texto(texto):
    texto = texto.upper()
    texto = texto.replace(" ", " ")
    texto = texto.strip()
    return texto

for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)

print(produtos)


# usando função map 

produtos_2 = list(map(padronizar_texto, produtos))

print(produtos_2)