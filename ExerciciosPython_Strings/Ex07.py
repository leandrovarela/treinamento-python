def contador_de_vogais_e_espaços():
    quantVogais= 0
    frase = input('Digite a frase: ')
    espaco = 0
    for indice in frase:
        print(indice)
        if indice == " ":
            espaco += 1
        if indice in "aeiou":
            quantVogais += 1

    print('Total de espaços em branco: %d' % espaco)
    print('Total de vogais: %d' % quantVogais)
