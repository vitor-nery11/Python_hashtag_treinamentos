from datetime import datetime
from zoneinfo import ZoneInfo

data_hora_atual = datetime.now()

print(data_hora_atual)

fuso_horario_sao_paulo = ZoneInfo("America/Sao_Paulo")
fuso_horario_ny = ZoneInfo("America/New_York")
fuso_horario_toquio = ZoneInfo("Asia/Tokyo")

data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
data_hora_toquio = data_hora_atual.astimezone(fuso_horario_toquio)

print(f"Data/hora em São Paulo: {data_hora_sao_paulo}")
print(f"Data/hora em Nova York: {data_hora_ny}")
print(f"Data/hora em Tóquio: {data_hora_toquio}")


def verifica_horario(data_hora):
    if 9 <= data_hora.hour < 17:
        return "aberto"
    else:
        return "fechado"

print(f"Escritório de São Paulo está {verifica_horario(data_hora_sao_paulo)}.")
print(f"Escritório de Nova York está {verifica_horario(data_hora_ny)}.")
print(f"Escritório de Tóquio está {verifica_horario(data_hora_toquio)}.")