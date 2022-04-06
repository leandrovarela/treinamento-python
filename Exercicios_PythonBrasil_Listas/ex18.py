


votos=[]

def vote_count():
    option=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    contagem=int(input("Número do jogador (0=fim): "))
    for i in range():

        if contagem == 0 :
            break
        elif contagem not in option: 
            print("Valor inválido")

        return votos.append(contagem)

def print_status():
    voto=votos
    print("\n---------------Exercício 18-----------------")
    print("\n Resultado da votação:")
    print(f"Foram computados {len(votos)} votos")
    print("Sistema Operacional    Votos    %")

print(votos)

vote_count()
print_status()