# exercicios para definir categorias de bebidas 

def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False 
    


produtos = [
    'beb46275',
    'TFA23962',
    'TFA64715',
    'TFA69555',
    'TFA56743',
    'BSA45510',
    'TFA44968',
    'CAR75448',
    'CAR23596',
    'CAR13490',
    'beb46275',
    'beb46275',
    'beb46275',
    'beb46275',
]

for produto in produtos:
    if categoria(produto, 'BEB'):
        print(f'Enviar { produto} para o setor de bebidas alcolicas ')
    elif categoria(produto, 'BSA'):
        print(f'Enviar {produto} para o setor de bebidas não alcolicas')
        
