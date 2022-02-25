def main():
    print("\n---------------Exercício 06-----------------")
   
            

def calcula_notas():
    notas=[]
    alunos = []
    for aluno in range(10):
        print(aluno)
        if calcula_media(notas) >= 7.0:
            alunos.append(aluno)

            for index in range(4):
                notas.append(float(input(f"Insira a {index+1 } nota:  ")))
                print(notas)


def calcula_media(notas):
    media = []
    media_final= sum(notas)/ len(notas)
    print(media_final)
    media.append(media_final)
    
    
calcula_notas()
