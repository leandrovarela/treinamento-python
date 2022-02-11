def live_fitness_for_man_woman():
    print("\n------------------Execício 13------------------\n")

    altura =  float(input("Informe sua altura : "))

    calcula_peso_ideal_man = (72.7*altura) - 58
    calcula_peso_ideal_woman= (62.1*altura) - 44.7

    print(f"\nSeu peso ideal referente a sua altura é : {calcula_peso_ideal_man:,.2f} KG se for homem, se for uma mulher {calcula_peso_ideal_woman:,.2f}KG ")