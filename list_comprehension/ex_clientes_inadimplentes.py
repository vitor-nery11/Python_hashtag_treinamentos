# Adicionado o dia '15' no último cliente para corrigir o erro
clientes_devedores = [
    ('462.286.561-65', 14405, 24),
    ('251.569.170-81', 16027, 1),
    ('297.681.579-21', 8177, 28),
    ('790.223.154-40', 958, 15)  
]

clientes_inadiplentes = []

for cpf, valor, dia in clientes_devedores:
    if dia > 20:
        clientes_inadiplentes.append(cpf) 
        

print(clientes_inadiplentes)


# LIST COMPREHENSION

clientes_inadiplentes_2 = [cpf for cpf, valor, dia in clientes_devedores if dia > 20]
print(clientes_inadiplentes_2)