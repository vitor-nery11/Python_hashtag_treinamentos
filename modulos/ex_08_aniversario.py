from datetime import datetime

data_nascimento_usuario = input('informe sua data de nascimento (dd/mm/aaaa):')

print(data_nascimento_usuario)
print(type(data_nascimento_usuario))

data_nascimento_usuario = datetime.strftime(data_nascimento_usuario, '%d/%m/%Y')