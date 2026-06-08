funcionarios = [
    {"nome": "Ana", "salario": 3000},
    {"nome": "Carlos", "salario": 4500},
    {"nome": "João", "salario": 2500},
    {"nome": "Maria", "salario": 5000}
]

def gerar_relatorio(funcionarios):
    soma_salario = 0 
    maior_salario = 0 
    menor_salario = funcionarios[0]['salario']


    for funcionario in funcionarios:
        salario = funcionario['salario']

        soma_salario += salario


        if salario > maior_salario:
            maior_salario = salario

        if salario < menor_salario:
            menor_salario = salario

    media = soma_salario / len(funcionarios)
    qtd_funcionarios = len(funcionarios)

    return {
        'media':media,
        'Maior salario':maior_salario, 
        'Menor salario': menor_salario,
        'Quantidade de funcionarios': qtd_funcionarios
        }



print(gerar_relatorio(funcionarios))