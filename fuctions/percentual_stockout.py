

vendas = { 'v001' : (1500, 'concluido', ''), 
         'v002' : (1350, 'cancelado', 'Estoque em falta'),
         'v003' : (1400, 'cancelado', 'Estoque em falta'),
         'v003' : (1400, 'cancelado', 'Estoque em falta'),
         'v004' : (1500, 'concuido', '')

        }

def calculo_stockout(vendas):
    numerador = 0
    denominador = 0 
    for venda in vendas:
        valor,status,motivo = vendas[venda]
        print(vendas[venda])
        if status == 'concluido':
            denominador += valor
        elif status == 'cancelado' and motivo == "Estoque em falta":
            denominador += valor 
            numerador += valor
    return numerador / denominador

print(f'{calculo_stockout(vendas):.2%}')