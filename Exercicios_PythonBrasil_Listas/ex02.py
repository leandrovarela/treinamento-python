def ten_numbers_reals():
    print("\n---------------Exercício 02-----------------")
    
    lista_numeros_reais = []
    print ("Informe os 10 números reais")
    for contador in range(10):
        lista_numeros_reais.append(float(input(str(contador+1) +"º Número ""+" ":\n")))
        lista_numeros_reais.reverse()
    print (lista_numeros_reais) 