def separate_value(valor):
    print("\n---------------Exercício 19-----------------")
    print("O número analisado está inserido na chamada da função")
    
    numero = valor
    #numero = int(input('Digite um numero inteiro positivo: '))

    if numero <=1000 :

        # Extraindo a unidade
        unidade = numero % 10

        # Eliminando a unidade de nosso número
        numero = (numero - unidade)/10

        # Extraindo a dezena
        dezena = numero % 10

        # Eliminando a dezena do número original, fica a centena
        numero = (numero - dezena)/10
        centena = numero

        # Fazendo ser inteiros
        dezena = int(dezena)
        centena = int(centena)
        numero= int(numero)
        print(f"O número {valor} contém {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)")

    else:
        print("Numero inválido")
""""
separate_value(326)
separate_value(300)
separate_value(320)
separate_value(310)
separate_value(305)
separate_value(301)
separate_value(101)
separate_value(311)
separate_value(111)
separate_value(25)
separate_value(20)
separate_value(10)
separate_value(21)
separate_value(11)
separate_value(1)
separate_value(7)
separate_value(16)

"""