def nome_esta_na_lista(nome, lista):
    
    name = None
    for index, item in enumerate(lista):
        if nome == item["nome"]:
            name = lista[index]
    
    return name
