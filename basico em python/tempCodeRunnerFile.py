def consumo_do_carro():
  distancia = int(input("Quantos km voce andou?"))
  litros = int(input("Quantos litros de combustivel voce tinha?"))
  consumo = distancia / litros
  if consumo > 12:
    print("Seu consumo foi eficiente!")
  elif 12 >= consumo > 8:
    print("Seu consumo foi mediano.")
  else:
    print("Seu consumo foi alto!")

consumo_do_carro()