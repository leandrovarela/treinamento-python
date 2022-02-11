def live_fitness():
    print("\n------------------Execício 12------------------\n")
    
    altura =  float(input("Informe sua altura : "))

    calcula_peso_ideal = (72.7*altura) - 58

    print(f"\nSeu peso ideal referente a sua altura é : {calcula_peso_ideal:,.2f} Kg")
