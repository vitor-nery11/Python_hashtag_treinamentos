from datetime import datetime 

ultima_compra = datetime(2023, 5, 10)

data_hora_atual = datetime.now()

diferenca = data_hora_atual - ultima_compra

if diferenca.days > 30:
  print('Parabens, você ganhou um desconto!!!')

