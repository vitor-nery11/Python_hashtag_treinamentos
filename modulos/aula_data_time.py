from datetime import datetime

agora = datetime.now()

print(agora)

# pegando partes da data 

print(agora.day)
print(agora.month)
print(agora.year)
print(agora.hour)
print(agora.minute)
print(agora.second)

# criando uma data manualmente 

data = datetime(2026, 12, 25)

print(data)

# formatando datas 

agora = datetime.now()

print(agora.strftime('%d/%m/%Y'))

