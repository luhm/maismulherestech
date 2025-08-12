def cardapio():
  refeicao = {"Alimento": input("Qual alimento voce comeu? "), "Calorias": float(input("Quantas calorias tem esse alimento? "))}
  deseja_sair = bool(int(input("vc deseja sair [0 nao/1 sim]? ")))
  while deseja_sair == False:
    refeicao["Alimento": input("Qual alimento voce comeu? ")] = "Calorias": float(input("Quantas calorias tem esse alimento? "))
    deseja_sair = bool(int(input("vc deseja sair [0 nao/1 sim]? ")))
  print(refeicao)
  ver_historico = bool(int(input("Deseja ver seu historico de refeicoes? [0 nao/1 sim]? ")))
  if ver_historico == True:
     print(refeicao)
  else:
    pass
  
print(cardapio())