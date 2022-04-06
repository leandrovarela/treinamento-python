def data_por_extenso():
    data = input('Data de nascimento: ')
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    dia = int(data[0:2])
    mes = meses[int(data[3:5]) - 1]
    ano = int(data[6:])

    print('Você nasceu em %d de %s de %d' % (dia, mes, ano))