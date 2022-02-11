def point_average():
    print("\n---------------Exercício 05-----------------")
    
    nota_parc_1 = float(input("\nInsira a primeira nota do aluno :"))
    nota_parc_2 = float(input("\nInsira a segunda nota do aluno :"))
    media_aluno = float(nota_parc_1+nota_parc_2)/2
    
    
    if media_aluno == 10 :

        print("\nAprovado com Distinção")
    
    elif media_aluno >= 7:

        print("\nAprovado")
    else: 

        print("\nReprovado")