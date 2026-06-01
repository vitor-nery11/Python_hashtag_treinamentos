preço = 1500
custo = 400
lucro = 800

def carga_tributaria(preço,custo, lucro):
    imposto = preço - custo - lucro
    carga = imposto / preço 
    return carga 

print(f'a carga tributaria é de {carga_tributaria(preço,custo,lucro):.1%}')
