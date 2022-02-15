
from statistics import median


def print_sum_mean():
    print("\n-------------------Exercício 08--------------------\n")

    lista = [35,6,75,3,500]
    for valor in lista:
        maior =sum(lista)
        media =sum(lista)/len(lista)
    print(f"A soma dos valores foi: {maior}, e a média foi : {media}")
