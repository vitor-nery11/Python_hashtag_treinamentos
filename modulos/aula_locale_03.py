import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

numero = 1234567.89

print(locale.format_string("%.2f", numero, grouping=True))

