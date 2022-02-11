def year_bi():
    print("\n---------------Exercício 17-----------------")

    ano= int(input("\nInsira o ano que deseja saber se é bissexto ou não (YYYY):  "))

    if (ano%4 == 0 and ano%100 != 0) or (ano%400) == 0:

        print("\nCom certeza esse é um ano bissexto")

    else:

        print("\nEsse ano não é Bissexto")

        
