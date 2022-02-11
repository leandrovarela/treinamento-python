
def paint_store_2():
    print("\n------------------Execício 17------------------\n")
    
    area_a_decorar=float(input("Informe os metros² da área que deseja pintar: "))

    calcular_litros = (area_a_decorar/6)
    capacidade_lata = 18
    capacidade_galao = 3.6
    lata_18=  80.00
    galao_3_6= 25.00

    rendimento_lata = calcular_litros/capacidade_lata
    rendimento_galao = calcular_litros/capacidade_galao
    
    if rendimento_lata < 1:
        calcular_galao= rendimento_galao *galao_3_6
        print(f"\nR${calcular_galao:,.2f} este é o valor a ser gasto com {rendimento_galao:,.2f} de galões de tinta")
    
    elif rendimento_lata >= 1: 
       calcular_lata= rendimento_lata*lata_18 
       print(f"\nR${calcular_lata:,.2f} este é o valor a ser gasto com {rendimento_lata:,.2f} latas de tinta")

    else: 
        print("Deu merda capitão")

