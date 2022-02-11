def good_night():
    print("\n---------------Exercício 10-----------------")

    print("\nM-matutino ou V-Vespertino ou N-Noturno")
    turno= str(input("\nInsira o turno que você estuda: ").upper())

    if turno == "M":
        print("\nBom dia!")
    elif turno == "V":
        print("\nBoa Tarde!")
    elif turno == "N":
        print("\nBoa noite!")
    else:
        print("\nValor Inválido!")