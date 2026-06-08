usuarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
    {"id": 3, "nome": "João"}
]

def buscar_usuarios(usuarios,id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario
    
    return 'Usario não existe!!!'
        


print(buscar_usuarios(usuarios,5))