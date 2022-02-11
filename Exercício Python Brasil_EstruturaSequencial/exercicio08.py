def cash_for_hours():
    print("\n------------------Execício 08------------------\n")
    
    por_hora = float(input("\nInsira o Valor que ganha por hora : "))
    horas_trab = float(input("\nInsira a quantidade de horas trabalhadas: "))

    calcular = por_hora * horas_trab

    print(f"\nO Valor do seu salário é de R${calcular}")
