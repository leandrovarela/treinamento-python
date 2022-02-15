def not_duplicate():
    print("\n-------------------Exercício 02--------------------\n")
    print("Faça já seu cadastro:")
    usuario=str(input("Usuário: "))
    senha=str(input("Senha: "))
    while usuario==senha:
        print("ERRO: o usuário não pode ser igual a senha, tente novamente")
        usuario=str(input("Usuário: "))
        senha=str(input("Senha: "))
    else:
        print("Cadastrado efetuado com sucesso")
