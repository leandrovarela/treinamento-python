def validate_phone():
    print('Valida e corrige número de telefone')
    numero = int(input('Telefone: '))
    novo_numero = ''
    if len(str(numero)) < 8:
        diferenca = 8 - len(str(numero))
        novo_numero = '3' * diferenca

    numero_formatado = novo_numero + str(numero)
    numer_formatado = numero_formatado[0:4] + '-' + numero_formatado[5:]

    print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))
    print('Telefone corrigido sem formatação: %d' % numero)
    print('Telefone corrigido com formatação: %s' % numero_formatado)
