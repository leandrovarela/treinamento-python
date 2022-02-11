def final_average():
    print("------------------Execício 04------------------\n")
    name= input("Insira o nome do aluno: ")
    print("  \nInstrução: ------ Nota do aluno deve ser entre 0 e 10 -------Obs: Não use vírgula, use ponto.")
    note_1=float(input("\nInsira a primeira nota do aluno: "))
    note_2=float(input("\nInsira a segunda nota do aluno: "))
    note_3=float(input("\nInsira a terceira nota do aluno: "))
    note_4=float(input("\nInsira a quarta nota do aluno: "))
    
    soma= note_1+note_2+note_3+note_4 
    media= soma / 4
    
    print(f"\nA media final de {name} é {media}\n")
    
    
    