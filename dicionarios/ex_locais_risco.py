
# programa para avaliar a media de niveis de nitrogenio em cada região e alertar problemas
# Praticas sobre dicionarios em python



niveis_co2 = {
    'AC' : [324,405,429,486,402],
    'RJ' : [324,405,429,486,402],
    'AM' : [324,405,429,486,402]
}



for estado,valor in niveis_co2.items():
    itens_qtd = len(valor)
    total_c02 = sum(valor)
    media_c02 = total_c02 / itens_qtd
    
    if media_c02 > 450:
       print(f'{estado} esta com niveis altissimos de de CO2({media_c02}), chamar equipe especializada para verificar a região')




