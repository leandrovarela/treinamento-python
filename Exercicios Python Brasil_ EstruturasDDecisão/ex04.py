def vogal_or_consoante():
    print("\n---------------Exercício 04-----------------")
    
    dados= str(input("\nDigite uma Letra e saberá se é uma vogal ou consoante:  ").upper())
    lista_vogal=["A","E","I","O","U"]

    if dados in lista_vogal:
        print(f"\n{dados} é uma vogal")
    
    else:
        print(f"\n{dados} é uma consoante")