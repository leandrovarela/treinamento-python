def calculate_all_abonos():
    print('Digite 0 para encerrar o programa')
    salarios = [] 
    while True:
        salario = float(input('Salário: '))
        if salario == 0:
            break
        salarios.append(salario)

    print('Projeção de Gastos com Abono')
    print('============================')
    print('Salário - Abono')

    abonos, minimo = 0, 0
    maior = 0
    for salario in salarios:
        abono = salario * 0.2
        if abono < 100:
            abono = 100
            minimo += 1
        if abono > 100:
            maior = abono
        abonos += abono
        print('R$ %.2f - R$ %.2f' % (salario, abono))

    print('\nForam processados %d colaboradores' % (len(salarios)))
    print('3Total gasto com abonos: R$ %.2f' % abonos)
    print('Valor mínimo pago a %d colaboradores' % minimo)
    print('Maior valor de abono pago: R$ %.2f' % maior)
    
calculate_all_abonos()