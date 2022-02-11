def point_aprove():
    print("\n---------------Exercício 20-----------------")
    
    nota_parc_1 = float(input("\nInsira a primeira nota do aluno: "))
    nota_parc_2 = float(input("\nInsira a segunda nota do aluno: "))
    nota_parc_3 =float(input("\nInsira a terceira nota do aluno: "))
    
    media_aluno = float(nota_parc_1+nota_parc_2+nota_parc_3)/3
    
    
    if media_aluno == 10 :

        print(f"\nMédia:{media_aluno} Aprovado com Distinção")
    
    elif media_aluno >= 7:

        print(f"\nMédia:{media_aluno} Aprovado")
    else: 

        print(f"\nMédia:{media_aluno} Reprovado")


    