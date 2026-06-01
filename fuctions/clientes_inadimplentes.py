clientes_devedores = [
    ('035.880.825.14', 500, 20),
    ('123.456.789.01', 1500, 25),
    ('987.654.321.00', 800, 15),
    ('741.852.963.10', 2200, 30),
    ('159.357.486.20', 1200, 22),
    ('258.369.147.30', 950, 18),
    ('369.258.147.40', 3000, 45),
    ('456.123.789.50', 1100, 20),
    ('654.987.321.60', 700, 10),
    ('852.741.963.70', 1800, 28),
]

def devedores(clientes_devedores):
    lista_inadimplentes = []

    for cpf, valor, tempo in clientes_devedores:
        if valor >= 1000 and tempo >= 20:
            lista_inadimplentes.append(cpf)

    return lista_inadimplentes

print(devedores(clientes_devedores))
print(len(devedores(clientes_devedores)))