import numpy as np

'''
Requisitos
Mostrar a soma das notas de cada aluno.
Mostrar a soma das notas de cada prova.
Mostrar a média de cada aluno.
Mostrar a média de cada prova.
Descobrir a maior nota da matriz inteira.
Descobrir a menor nota da matriz inteira.
'''

notas = np.array([
    [7, 8, 9],
    [10, 6, 8],
    [5, 7, 6],
    [9, 9, 10]
])

soma_cada_aluno = notas.sum(axis=1)
soma_cada_prova = notas.sum(axis=0)
media_aluno = notas.mean(axis=1)
media_prova = notas.mean(axis=0)
maior_nota = notas.max()
menor_nota = notas.min()


print(f'A soma das notas de cada aluno é respectivamente: {soma_cada_aluno}')
print(f'A soma de notas de cada prova é: {soma_cada_prova}')
print(f'media de cada aluno: {media_aluno}')
print(f'Media de cada prova: {media_prova}')
print(f'A maior nota da lista é: {maior_nota}')
print(f'A menor nota da lista é: {menor_nota}')

