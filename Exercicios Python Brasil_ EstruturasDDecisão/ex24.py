def mult_types():
    print("\n---------------Exercício 24-----------------")


    numero_01= int(input("\nInsira um número:"))
    numero_02= int(input("\nInsira outro número: "))
    digite= str(input("\nA para operação : par ou ímpar\n\nB para operação: positivo ou negativo\n\nC para operação: inteiro ou decimal\n\nEscolha: ").upper())

    if digite == "A":
        if (numero_01%2) == 0:
            print(f"\nO numero {numero_01} é um numero par") 
        
        else:
            print(f"\nO número {numero_01} é um numero ímpar")
            
        if (numero_02%2) == 0:

            print(f"\nO numero {numero_02} é um numero par") 
        else:
            print(f"\nO número {numero_02} é um numero ímpar")
        
    elif digite == "B":

        if numero_01 > 0:
        
            print(f"\nEsse numero {numero_01},é Positivo")
        else: 
            print(f"\nEsse numero{numero_01}, é Negativo")

        if numero_02 > 0:
            print(f"\nEsse numero {numero_02}, é Positivo")

        else: 
            print(f"\nEsse numero {numero_02}, é Negativo")
        

    elif digite == "C":

        if numero_01 % 1 == 0:
            print(f"\n{numero_01} É um número inteiro")

        else:
            print(f"\n{numero_01} É um número decimal")

        if numero_02%1 == 0:
            print(f"\n{numero_02} É um número inteiro")

        else:
            print(f"\n{numero_02} É um número decimal")
    else: 
        print("Valor inválido")


