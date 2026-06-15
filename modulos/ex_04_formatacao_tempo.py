import time  # bilioteca para mexer com time 
import locale # biblioteca para mexer com localização e formatações 

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # comanmdo para formatar dados em PT-BR

tempo_em_struc = time.localtime()

tempo_formatado = time.strftime('%A, %d  de %B %Y', tempo_em_struc)
print(tempo_formatado)