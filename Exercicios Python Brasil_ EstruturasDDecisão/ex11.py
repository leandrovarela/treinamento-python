def payment_pl():
    print("\n---------------Exercício 11-----------------")
    salario = float(input("\nDigite o seu salário: R$"))
    aumento_absoluto = 0
    aumento_relativo = 0
    salario_liquido = 0

    print("Antes Reajuste: ", salario)

    if salario <= 280:
        aumento_relativo = 0.20

    elif salario > 200 and salario <= 700:
        aumento_relativo = 0.15

    elif salario > 700 and salario <= 1500:
        aumento_relativo = 0.10
    else:

       aumento_relativo = 0.05
       
    aumento_absoluto = salario * aumento_relativo
    salario_liquido = salario * (1 + aumento_relativo)
    print(f"Aumento: {aumento_relativo * 100}%\nValor: ", aumento_absoluto, "\nFinal: ",salario_liquido)