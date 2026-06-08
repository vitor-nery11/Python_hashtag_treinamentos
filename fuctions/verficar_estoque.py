estoque = {
    "Notebook": 10,
    "Mouse": 3,
    "Teclado": 0,
    "Monitor": 5
}



def verificar_estoque(estoque):
    for produto,quantidade in estoque.items():
        if quantidade <= 5:
            print(f'{produto} - {quantidade}: É preciso verificar esse produto!!')
        else:
            print(f'{produto} - {quantidade}: esta dentro do esperado')
            

verificar_estoque(estoque)