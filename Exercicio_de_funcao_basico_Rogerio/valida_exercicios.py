import exercicio1
import exercicio2

sucesso_unicode_char = "\u2705"
falha_unicode_char = "\u274C"

def valida_exercicio1():
    print(f"\nValidando exercicio 1...")
    lista = [1,2,7,0,342,87,-98,25]
    resultados_esperados = [
        (1,True),
        (2,True),
        (7,True),
        (0,True),
        (342,True),
        (-98,True),
        (40,False),
        (123,False),
    ]
    
    for cenario in resultados_esperados:
        if exercicio1.elemento_esta_na_lista(cenario[0],lista) == cenario[1]:
            print(f"Teste {cenario} passou {sucesso_unicode_char}")
        else:
            print(f"Teste {cenario} falhou {falha_unicode_char}")
            
            
def valida_exercicio2():
    print(f"\nValidando exercicio 2...")
    lista = [
        {
            "nome": "Rogerio",
            "telefone": "132456789"
        },
        {
            "nome": "Fulano",
            "telefone": "102456789"
        },
        {
            "nome": "Beltrano",
            "telefone": "232456789"
        },
    ]
    resultados_esperados = [
        ("Rogerio",lista[0]),
        ("Fulano",lista[1]),
        ("Beltrano",lista[2]),
        ("Anonimo",None),
        ("Anonimo II",None),
    ]
    
    for cenario in resultados_esperados:
        resultado = exercicio2.nome_esta_na_lista(cenario[0],lista)
        
        if resultado:
            if resultado.get("nome") == cenario[0] and resultado.get("telefone") == cenario[1].get("telefone"):
                print(f"Teste {cenario} passou {sucesso_unicode_char}")
            else:
                print(f"Teste {cenario} falhou {falha_unicode_char}")
                
        else:
           if resultado == cenario[1]:
               print(f"Teste {cenario} passou {sucesso_unicode_char}")
           else:
               print(f"Teste {cenario} falhou {falha_unicode_char}")
    
    