# Fatec São Paulo, Curso ADS Noturno, 1º / 2020.
# IAL 002: Projeto Programa nº4
# Entrega 13/07/2020
#
# 20100738 Christian Satio Cubo
# 20111105 Davi Silva Costa
# 20100711 Eugenio Dalle Olle
# 20111123 Rennan Ferruzzi Izarchi
# 20119491 Vitor Macedo de Medeiros
# 20118320 Vanderson Xavier Barbosa
# XXXXXXXX Max Gabriel Vargas

# Função para gerar o arquivo de dados dos produtos
# NÃO ENTREGAR JUNTO COM OS OUTROS
from random import randint

def GeraProdutos(nomearq,qtd):
  '''Gera um arquivo com valores aleatóreos formatados corretamente.\nEntre com o nome do arquivo e a quantidade de itens no arquivo.\nRetorna o nome do arquivo.'''

  Dados = []

  i = 0
  while i < qtd - 4: # -4 para incluir os dados como exemplo no PDF
    a = randint(10000, 99999)
    b = randint(1, 2)
    c = randint(1, 999999)/1000
    d = randint(1, 9999)/100
    e = randint(100, 4999)/100

    if b == 1:
      b = "P"
    elif b == 2:
      b = "U"
      c = round(c, 0)
      
    Dados.append((a, b, c, d, e))
    i = i + 1
  
  arq = open(nomearq, "w")
  for item in Dados:
    arq.write("{};{};{:.3f};{:.2f};{:.2f}\n".format(item[0], item[1], item[2], item[3], item[4]))
  arq.close
  print("Arquivo gerado com sucesso: ",nomearq)
  return nomearq

a = GeraProdutos("PRODUTOS.TXT", 15)

