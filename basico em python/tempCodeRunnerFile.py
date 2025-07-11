
def cardapio():
  refeicao = {"Alimento": input("Qual alimento voce comeu? "), "Calorias" : float(input("Quantas calorias tem esse alimento? "))}
  deseja_sair = bool(input("vc deseja sair [0 nao/1 sim]?"))
  if deseja_sair: 
    pass
  else:
    refeicao.update({"Alimento": input("Qual alimento voce comeu? "), "Calorias" : float(input("Quantas calorias tem esse alimento? "))})

print(cardapio())