meta = 10000

vendas = {
    'joão': 15000,
    'julia': 27000,
    'Marcus': 9900,
    'Maria' : 3850,
    'Alon' : 7878,
}


def calculo_meta(meta,vendas):
    vencedores = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            vencedores.append(vendedor)
        per_beteram_meta = len(vencedores ) / len(vendas)

    
    return vencedores, per_beteram_meta

vencedores, percentual = calculo_meta(meta,vendas)

print(vencedores)
print(f'{percentual:.1%}')



