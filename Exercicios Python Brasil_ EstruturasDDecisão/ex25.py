def detetive():
    print("\n---------------Exercício 25-----------------")
    perguntas=["\nTelefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","Já trabalhou com a vítima? "]
    resp =[]

    print("\nResponda apenas com sim ou não: ")
    for pergunta in perguntas:
        print(pergunta)
        perg =str(input("Resp: "))
        
        if perg == "sim" or perg == "não":
            resp.append(perg)
        else: 
            print("valor inválido")

    pontos = resp.count("sim")

    if pontos == 2:

        print("\nClassificado como: Suspeito")

    elif pontos == 3 or pontos == 4:

        print("\nClassificado como: Cúmplice")

    elif pontos == 5:

        print("\nClassificado como: Assassino")

    elif pontos == 0 or pontos == 1:

        print("\nClassificado como: Inocente")
    else:

        print("Valor inválido")

