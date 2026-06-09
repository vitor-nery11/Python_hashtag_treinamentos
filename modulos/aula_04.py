import time

inicio = time.time()

for i in range(1000000):
    pass

fim = time.time()

print(f'tempo gasto: {fim -inicio:.4f} segundos ')
