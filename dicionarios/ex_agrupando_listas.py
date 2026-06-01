produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell']

vendas2019 = [558147, 712350, 573823, 402522, 718654, 351580, 973139, 892292, 422760, 154753, 880601, 438508, 237467, 497805]

vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644]

vendas = list(zip(vendas2019,vendas2020))

vendas_produtos = dict(zip(produtos,vendas))
print(vendas_produtos)
