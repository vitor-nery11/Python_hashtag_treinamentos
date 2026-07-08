import numpy as np
'''
Seu gerente pediu um relatório.

Requisitos

Escreva um programa que mostre:

Todos os alunos que levantaram mais de 70 kg.
Todos os alunos que levantaram 50 kg ou menos.
Todos os alunos que levantaram exatamente 60 kg.
Todos os alunos que levantaram valores diferentes de 75 kg.
'''

pesos = np.array([40, 55, 60, 75, 80, 45, 90, 100, 65, 50])

print(pesos[pesos>70])
print(pesos[pesos<=50])
print(pesos[pesos==60])
print(pesos[pesos!=75])

