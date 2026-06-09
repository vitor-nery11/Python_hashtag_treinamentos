import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

valor = 1500.75

print(locale.currency(valor, grouping=True))