import time 

nada = input('Aguardando o usuario apertar enter para iniciar:')

inicio = time.time()

nada_1 = input('aparte novamente para finalizar')

fim = time.time()

resultado = fim - inicio

print(f'Tempo cronometrado é de: {resultado:.4f} segundos')
