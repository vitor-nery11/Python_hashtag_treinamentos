notas = [7, 8, 5, 10, 4, 6, 9]

# media = 7
# maior nota
# menor nota 
# aprovado 
# reprovado

def avaliador(notas):
    maior_nota = 0
    menor_nota = 10

    media = sum(notas) / len(notas)

    aprovado = ''
    reprovado = ''
    
    for nota in notas:
        # logica para aprovação
        if media >= 7:
            aprovado = 'Esse aluno foi aprovado!!'
        else:
            reprovado = 'Esse aluno foi reprovado'

        # Maior nota e menor nota

        if maior_nota < nota:
            maior_nota = nota
          
        if menor_nota  > nota:
            menor_nota = nota

    return media,maior_nota,menor_nota,aprovado,reprovado
        
print(avaliador(notas))
        