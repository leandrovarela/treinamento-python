def comparar_consumo_veiculos(quant_carros):
    modelos=[]
    consumos= []

    for i in range(1,quant_carros+1):
        print('Veículo %d' % i)
        modelos.append(input('Nome: '))
        consumos.append(float(input('Km por litro: ')))

    print("\n Relatório Final \n")
    cont, custo = 0, 0
    gasto = 0
    menorModelo = ''
    menor = 0
    for m in modelos:
        custo = 1000 / consumos[cont]
        gasto = custo * 2.25
        print('%s      - %.1f  -  %.1f litros  - R$ %.2f' % (m, consumos[cont], custo, gasto))
        if cont == 0:
            menor = custo
            menorModelo = m

        if custo < menor:
            menor = custo
            menorModelo = m
        cont += 1
    print('O menor consumo é do %s.' % (menorModelo))

comparar_consumo_veiculos(5)
