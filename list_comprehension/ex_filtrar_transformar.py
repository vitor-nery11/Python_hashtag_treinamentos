idades = [12, 18, 15, 25, 30, 16, 40]

maior_idade = []

for idade in idades:
    if idade >= 18:
        transformado = idade * 2
        maior_idade.append(transformado)


print(maior_idade)

# LIST COMPREHENSION

maior_idade_2 = [idade * 2 if idade >= 18 else 0  for idade in idades]

print(maior_idade_2)