vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400}
meta = 1000

bonus = []

for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)


# LIST COMPREHENSION 
bonus_2 = [vendedores_dic[item] * 0.1  if vendedores_dic[item] > meta else 0 for item in vendedores_dic]

print(bonus) 
print(bonus_2)
        
