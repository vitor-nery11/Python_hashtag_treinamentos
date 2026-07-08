import numpy as np 

dados = [127, 90,201, 150, 210,220,215]

vendas = np.array(dados)
print(vendas)
media_vendas = np.mean(vendas)
print(f'a media de vendas dos sete dias foi de {media_vendas:.2f}')