def box_cash(carros):
    modelos=[]
    consumos= []

    for i in range(1,carros):
        print('Veículo %d' % i)
        modelos.append(input('Nome: '))
        consumos.append(float(input('Km por litro: ')))

    print('Relatório Final')
    cont, custo = 0, 0
    gasto = 0
    menorModelo = ''
    menor = 0
    for m in modelos:
        print(m)
        custo = 1000 / consumos[cont]
        gasto = custo * 2.25
        print('%s      - %.1f  -  %.1f litros  - R$ %.2f' % (m, consumos[cont], custo, gasto))
        if cont == 0:
            menor = custo
            menorModelo = m
        if menor < custo:
            menor = custo
            menorModelo = m
        cont += 1
    print('O menor consumo é do %s.' % (menorModelo))
box_cash(5)