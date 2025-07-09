'''
DESAFIO 1

Peça o número de páginas lidas em um dia:

A: 50 ou mais → Leitor voraz

B: 30 a 49 → Ótimo ritmo

C: 10 a 29 → Leitura moderada

D: menos de 10 → Leitura leve
'''

# RESPOSTA

def tipo_de_leitor():
  numero_de_paginas = int(input("Quantas páginas voce leu? "))
  if numero_de_paginas > 50:
    print("Leitor voraz")
  elif 49 > numero_de_paginas > 30:
    print("Ótimo ritmo")
  elif 29 > numero_de_paginas > 10:
    print("Leitura moderada")
  else:
    print("Leitura leve")

tipo_de_leitor()

'''
DESAFIO 3

O computador escolhe um número entre 1 e 50.

O usuário tem apenas 5 tentativas para adivinhar. Se acertar, parabéns! Se não, o jogo acaba e revela o número.
'''

import random

def advinhar_numero():
  numero = int(input("Tente advinhar o numero: "))
  numero_aleatorio = random.randint(1, 50)
  contador = 0
  while contador <= 5:
    if numero_aleatorio != numero:    
      print(int(input("Tente de novo: ")))
    else:
      print("Parabens!")
    contador = contador + 1
  print(f"Voce perdeu. O numero era {numero_aleatorio}")

advinhar_numero()


'''
DESAFIO 4

Permita:

Adicionar um alimento (nome, calorias)

Registrar refeições do dia

Ver total de calorias consumidas

Ver histórico alimentar

Sair
'''

# permita = usar input

# (nome, calorias) = dicionário

# Registrar refeições do dia = cada refeicao é um novo dicionario

# total de calorias consumidas = soma dos values

# historico alimentar = ver todas as keys

'''
DESAFIO 5

Peça ao usuário a distância percorrida (km) e o total de combustível gasto (litros). Calcule o consumo médio: Consumo = distância / litros

Classifique o consumo:

Menor que 8 km/l: Consumo alto

Entre 8 e 12 km/l: Consumo médio

Maior que 12 km/l: Consumo eficiente
'''

def consumo_do_carro():
  distancia = int(input("Quantos km voce andou? "))
  litros = int(input("Quantos litros de combustivel voce tinha? "))
  consumo = distancia / litros
  if consumo > 12:
    print("Seu consumo foi eficiente!")
  elif 12 >= consumo > 8:
    print("Seu consumo foi mediano.")
  else:
    print("Seu consumo foi alto!")

consumo_do_carro()

