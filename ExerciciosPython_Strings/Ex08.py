def yes_or_no_palindrono():
    palavra = input('Digite a palavra: ').upper()

    nova_palavra = ''
    for index in palavra:
        if index != ' ':
            nova_palavra += index
            
    if nova_palavra == nova_palavra[::-1]:
        print('É um palíndromo!')
    else:
        print('Não é palíndromo!')
yes_or_no_palindrono()
