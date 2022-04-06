from random import randint

def craps():
    dado = randint(2,13)
    if dado == 7 or dado == 11:
        print('Você um natural e ganhou!')

    elif dado == 2 or dado == 3 or dado == 12:
        print('Craps você perdeu!')

    elif dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado ==10:

        numero = 0
        while dado != numero:
            numero = randint(2,13)
            if numero == 7:
                print('Você perdeu!')
                break
        if numero != 7:
            print('Você ganhou!')