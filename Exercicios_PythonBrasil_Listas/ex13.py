def fire_of_years():
    print("\n---------------Exercício 13-----------------")
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    temperatura = []

    for mes in range(0, len(meses)):
        temperatura.append(float(input(f"\nInsira a temperatura de {meses[mes]} : ")))
        mediaAnual = sum(temperatura)/len(temperatura)
    
    print("\nOs meses com as temperaturas acima da média anual foram :\n")
    for me in range(0, len(temperatura)):
        if temperatura[me] > mediaAnual:
            print (str(me+1) + " - " + meses[me])

