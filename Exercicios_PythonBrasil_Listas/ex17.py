def media_saltos():
    print("\n---------------Exercício 17-----------------")
    saltos=["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
    notas=[]
    nome=input("Nome: ")
    
    if nome != "":
        for i in saltos:
            nota=float(input(f"{i} salto: "))
            notas.append(nota)
        media=sum(notas)/len(notas)    
        print("\nResultado final: ")
        print(f"Atleta:{nome}")
        print(f"\nSaltos: {notas[0]} - {notas[1]} - {notas[2]} - {notas[3]} - {notas[4]}")
        print(f"\nMédia dos Saltos: {media} m")  
        
    elif nome == "":
        print("")
        
            
media_saltos()
