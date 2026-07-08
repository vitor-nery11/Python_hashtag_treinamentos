import numpy as np 

precos = np.array([31.40,31.25,30.95,31.20,31.60,31.50])

preco_maximo = np.max(precos)
preco_minimo = np.min(precos)
variacao_preco = preco_maximo - preco_minimo
print(preco_maximo)
print(preco_minimo)
print(variacao_preco)