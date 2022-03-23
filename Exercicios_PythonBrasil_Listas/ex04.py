def separa_consoantes(lista_caracteres):
    vogais=["a","e","i","o","u"]
    
    consoante = lambda item : item.lower() not in vogais
    #Mesma coisa do codigo abaixo
    # def consoante(item):
    #     return item not in vogais
    return list(filter(consoante, lista_caracteres))
    
def format_print(consoantes):
    
    print(f"\nForam lidas {len(consoantes)} consoantes: {consoantes} ")       

consoantes = separa_consoantes(['b', 'N', 'y', 'i', 'o', 'x', "I"])
format_print(consoantes)
       
