import numpy as np

'''
Requisitos
Mostrar todos os alunos aprovados (nota >= 7).
Mostrar todos os alunos reprovados (nota < 7).
Mostrar os alunos que tiraram nota entre 7 e 9, inclusive.
Mostrar quantos alunos foram aprovados.
Mostrar quantos alunos foram reprovados.
Mostrar a maior nota.
Mostrar a menor nota.
Mostrar a média da turma.
'''

notas = np.array([4.5, 7.0, 8.5, 5.5, 9.0, 6.0, 3.5, 10.0, 7.5, 8.0])

aprovados = notas[notas>=7]
reprovados = notas[notas < 7] 
alunos_entre_7_e_9 = notas[(notas >= 7) & (notas <= 9)]
quantidade_aprovados = np.sum(notas>=7)
quantidade_reprovados = np.sum(notas < 7)
maior_nota = notas.max()
menor_nota = notas.min()
media_notas = notas.mean()

print(f'A nota dos aprovados foram as seguintes: {aprovados}')
print(f'A nota dos reprovados foram as seguintes: {reprovados}')
print(f'Alunos com notas entre 7 e 9: {alunos_entre_7_e_9}')
print(f'O numero de alunos aprovados foi de: {quantidade_aprovados}') 
print(f'O numero de alunos reprovados foi de: {quantidade_reprovados}')
print(f'A maior nota foi: {maior_nota}')
print(f'A menor nota foi: {menor_nota}')
print(f'A media de notas foi: {media_notas}')
