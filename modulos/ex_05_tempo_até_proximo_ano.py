import time 
import locale 

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

tempo_atual = time.localtime()
print(tempo_atual )

tempo_ano_novo = (tempo_atual.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)
print(tempo_ano_novo)

segundos_restantes = int(time.mktime(tempo_ano_novo)) - time.mktime(tempo_atual)
print(segundos_restantes)

segundos_por_minuto = 60 
segundos_por_hora = 60 * 60 
segundos_por_dia = 24 * 60 * 60 

dias, resto_segundos = divmod(segundos_restantes, segundos_por_dia)

print(dias)
print(resto_segundos)

horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)
minutos, segundos = divmod(resto_segundos, segundos_por_minuto)

print(horas)
print(minutos)
print(segundos)

print(f'Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos')