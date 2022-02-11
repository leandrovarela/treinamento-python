
def paint_store():
    
    print("\n------------------Execício 16------------------\n")
    area_a_decorar=float(input("Informe os metros² da área que deseja pintar: "))

    calcular_litros = (area_a_decorar/3)
    capacidade_lata = 18
    preco= 80.00

    rendimento_lata = calcular_litros/capacidade_lata
    valor_final= preco * rendimento_lata
    print(f"\n Você utilizará o total de  {rendimento_lata:,.2f} lata(s) para decorar tudo, e isso custará R${valor_final:,.2f}")



    