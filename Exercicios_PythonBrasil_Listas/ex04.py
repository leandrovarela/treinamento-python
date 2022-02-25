def vogal_or_consoante():
    print("\n---------------Exercício 04-----------------")
    vogal=["a","e","i","o","u"]
    consoante =[]
    for caracteres in range(10):
        caract=str(input("\nInsira um caracter: "))
        if caract not in vogal:
            consoante.append(caract)

    print(f"\nForam lidas {len(consoante)} consoantes ")       
vogal_or_consoante()            
