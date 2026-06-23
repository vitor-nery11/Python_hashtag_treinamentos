numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_pares.append(0)

print(numeros_pares)

# LIST COMPREHENSION 

numeros_pares_2 = [ numero if numero % 2 == 0 else 0 for numero in numeros ]

print(numeros_pares_2)