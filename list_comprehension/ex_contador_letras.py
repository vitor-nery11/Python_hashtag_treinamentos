palavras = ["python", "java", "javascript", "c", "go", "typescript"]

letras_testadas = []

for palavra in palavras:
    if len(palavra) > 4:
        letras_testadas.append(palavra)

print(letras_testadas)


# LIST COMPREHENSION 

letras_testadas_2 = [palavra if len(palavra) > 4 else 0 for palavra in palavras]

print(letras_testadas_2)