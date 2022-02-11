def speed_test():

    print("\n------------------Execício 18------------------\n")
    tamanho = float(input('Tamanho do arquivo (MB): '))
    velocidade = float(input('Velocidade de Internet (MBps): '))

    calcular_tempo_transfer= (tamanho/velocidade)*60

    print(f"\nTempo aproximado de download: {calcular_tempo_transfer:,.2f} Minutos ")
