
def eh_par(numero):
    return numero %2 == 0

def separa_pares_e_impares(lista_numeros):
    pares = list(filter(eh_par,lista_numeros))
    impares = list(filter(lambda x: not(eh_par(x)), lista_numeros))
    
    return pares, impares
    
def imprime_vetores(vetor_original, pares, impares):
    print("\n---------------Exercício 05-----------------")
    print(f"Os números do vetor são {vetor_original}")
    print(f"Os números pares são {pares}")
    print(f"Os números impares são {impares}")
    

lista = [1,90,45,13,4,7,13]
imprime_vetores(lista, *separa_pares_e_impares(lista))
