from cgi import print_directory


votos=[]

def vote_count():
    voto=[]
    option=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    while True:
        contagem=int(input("Número do jogador (0=fim): ")) 
        if contagem == 0 :
            break
        elif contagem in option:
            voto.append(contagem)
        else:
            print("Valor inválido")

    return voto

def print_status():
    voto=votos
    print("\n---------------Exercício 18-----------------")
    print("\n Resultado da votação:")
    print(f"Foram computados {len(votos)} votos")
    print("Sistema Operacional    Votos    %")

print(votos)

vote_count()
print_status()