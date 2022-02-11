def calculate_impost():
    print("\n------------------Execício 15------------------\n")

    ganho_por_hora = float(input("Quanto ganha por hora? "))
    horas_trabalhadas = float(input("\nHoras trabalhadas por mês: "))

    salario_bruto = ganho_por_hora * horas_trabalhadas
    imposto_rend = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido= (salario_bruto - imposto_rend - inss - sindicato)

    print (f"\nSalário Bruto : R$ {salario_bruto:,.2f}")
    print (f" IR: R$ {imposto_rend:,.2f}" )
    print (f" INSS: R${inss:,.2f}" )
    print (f" Sindicato: R$ {sindicato:,.2f}")
    print (f" Salário Liquido : R${salario_liquido:,.2f}")