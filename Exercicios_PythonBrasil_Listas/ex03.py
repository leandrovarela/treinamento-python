def man_or_woman():
    print("\n---------------Exercício 03-----------------")
    
    notas=[]
    for nota in range(4):
        note= float(input("Insira a nota: "))
        notas.append(note)

    result= sum(notas) / len(notas) 
    print (f"A média é {result} e as notas são {notas}")
man_or_woman()

