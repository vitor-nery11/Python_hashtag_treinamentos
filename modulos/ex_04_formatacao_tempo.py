import time 
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

tempo_em_struc = time.localtime()

tempo_formatado = time.strftime('%A, %d  de %B %Y', tempo_em_struc)
print(tempo_formatado)