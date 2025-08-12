def cardapio():
    historico = []

    while True:
        alimento = input("Qual alimento você comeu? ")
        calorias = float(input("Quantas calorias tem esse alimento? "))
        
        refeicao = {"Alimento": alimento, "Calorias": calorias}
        historico.append(refeicao)

        deseja_sair = input("Deseja adicionar outro alimento? [s/n]: ").strip().lower()
        if deseja_sair == 'n':
            break
   
    ver_historico = input("Deseja ver seu histórico de refeições? [s/n]: ").strip().lower()
    if ver_historico == 's':
        print("\nHistórico de Refeições:")
        total_calorias = 0
        for idx, item in enumerate(historico, 1):
            print(f"{idx}. Alimento: {item['Alimento']}, Calorias: {item['Calorias']}")
            total_calorias += item['Calorias']
        
        print(f"\nTotal de calorias consumidas: {total_calorias} kcal")

cardapio()
