frase = "python é muito legal e python é poderoso"



def contador_de_palavras(frase):
   contador = {
   
}
   
   resultado = frase.split()
   for palavra in resultado:
      if palavra not in contador:
         contador[palavra] = 1
      else:
         contador[palavra] += 1

   return contador


print(contador_de_palavras(frase))