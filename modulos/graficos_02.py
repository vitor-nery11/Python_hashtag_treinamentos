import matplotlib.pyplot as plt
import numpy as np

venda = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.plot(meses, venda)
plt.axis([0, 50, 0, max(venda)+ 200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()

# Mudando linhas para marcadores 
plt.plot(meses, venda, 'ro')
plt.axis([0, 50, 0, max(venda)+ 200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()

# Grafico de dispersão 
plt.scatter(meses,venda)
plt.show()

# Grafico de barras 
plt.bar(meses,venda)
plt.show()
