estoque = [('BSA2199', 396), ('PPF5239', 251), ('BSA1212', 989), ('PPF2154', 449), ('BEB3410', 241), ('PPF8999', 527), ('EMB9591', 601)]

lista_compras = []

for id, quantidade in estoque:
    if quantidade < 200:
        lista_compras.append(1000)
    else:
        lista_compras.append(500)


# LIST COMPREHENSION

lista_compras_2 = [1000 if quantidade < 200 else 500  for id, quantidade in estoque]


print(lista_compras)        
print(lista_compras_2)    