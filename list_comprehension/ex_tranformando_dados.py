nomes = ["ana", "joao", "maria", "carlos"]

lista_transformada = []

for nome in nomes:
    lista_transformada.append(nome.upper())

print(lista_transformada)


# LIST COMPREHENSION 

lista_transformada_2 = [nome.upper() for nome in nomes]


print(lista_transformada_2)